import os
from dotenv import load_dotenv
import datetime

# LangChain components for RAG
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# --- 1. Configuration: Load API Key and Initialize Models ---
load_dotenv() # Load GOOGLE_API_KEY from your .env file

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please set it.")


# Initialize the Embeddings Model (MUST be the SAME as used for creating the DB)
# 'models/embedding-001' is common for text.
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
print("Initialized Google Gemini Embeddings model.")


# Initialize the LLM (Gemini Pro is a good general-purpose choice)
# You can switch to "gemini-1.5-flash" for potentially faster/cheaper responses
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
print("Initialized Google Gemini LLM (gemini-pro).")


# --- 2. Load the Existing Vector Store ---
PERSIST_DIRECTORY = "./chroma_db"
print(f"Loading ChromaDB vector store from '{PERSIST_DIRECTORY}'...")


# Load the existing vector store using the same embeddings model
vector_store = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embeddings_model # Crucial: use the same embeddings!
)
print("ChromaDB vector store loaded successfully.")


# --- 3. Set up the Retriever ---
# This will search your vector store for relevant documents based on the query.
# k=3 means it will retrieve the top 3 most relevant chunks. You can adjust this.
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
print("Retriever set up.")

# --- Dynamic Date Insertion ---
def get_current_date_formatted():
    """Returns the current date formatted as 'Month Day, Year'."""
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

current_date_string = get_current_date_formatted()
print(f"Current date for bot context: {current_date_string}")

# - Adding memory for the chat
memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True
)


# --- 4. Define the Prompt Template ---
# This prompt instructs the LLM on how to answer questions using the provided context.
# The `context` will be dynamically inserted by the RAG chain.
template = """
**Today's Date:** {current_date}
**Persona:** You are Alex Gu. You are an easy-going and friendly individual, but you are also highly serious and meticulous about your work and accomplishments. Speak in a confident and professional manner, but with a conversational and non-robotic tone. Your goal is to be helpful, informative, and engaging.

**Instructions:**
1.  **Perspective:** You are speaking in the first person ("I," "my," "we") from the perspective of today's date. When referencing past events, speak in the past tense and correctly contextualize them with their dates.
2.  **Contextual Use:** Use ONLY the provided context to answer questions. Do not fabricate information.
3.  **Source Hierarchy:**
    * For general or summary questions (e.g., "What projects have you worked on?"), prioritize and synthesize information from documents with "overview" in their name.
    * For detailed or specific questions, use the full project or experience documents.
4.  **Response Format:**
    * Keep answers concise but comprehensive enough to directly address the question.
    * End your response by politely asking if they would like to know more about a specific topic.
5.  **Handling Ambiguity:** If a question is too vague (e.g., "Tell me more about that"), politely ask for more specific details (e.g., "Which project or experience would you like to know more about?").
6.  **Lists:** When answering questions that ask for lists, please extract the list directly from the context if present, and present it clearly, perhaps using bullet points or numbered lists.
7.  **Disclaimer:** You are interacting with an AI. Some information may be incorrect. For serious inquiries, please contact me directly.

**Conversation History:**
{chat_history}

**Context:**
{context}

**Question:** {question}

**Answer:**
"""
prompt = ChatPromptTemplate.from_template(template)
print("Prompt template defined.")


# --- 5. Assemble the RAG Chain using LCEL ---
# LCEL allows you to chain different components together in a clean, readable way.
# - "context": The `RunnablePassthrough()` makes sure the original input (question)
#              is passed through to the retriever, which then returns the context documents.
# - "question": The `RunnablePassthrough()` takes the original user question.
# - These two are passed as a dictionary to the prompt.
# - The prompt's output (a formatted message for the LLM) is passed to the LLM.
# - The LLM's raw output is then parsed into a string.
rag_chain = (
    {
        "context": retriever, 
        "question": RunnablePassthrough(),
        "current_date": RunnablePassthrough(lambda x: current_date_string)
    }
    | prompt
    | llm
    | StrOutputParser()
)
print("RAG chain assembled.")


# --- 6. Implement the Query Logic (Interactive Chat Loop) ---
print("\n--- Alex Gu Bot ---")
print("Ask me anything! (type 'bye' to quit).")

while True:
    user_query = input("\nYour question: ")
    if user_query.lower() == 'bye':
        print("Goodbye!")
        break

    try:
        # Invoke the RAG chain with the user's question
        response = rag_chain.invoke(user_query)
        print(f"Bot: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again or check your API key/internet connection.")