import os
from dotenv import load_dotenv
import datetime

# LangChain components for RAG
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

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
retriever = vector_store.as_retriever(search_kwargs={"k": 15})
print("Retriever set up.")

# --- Dynamic Date Insertion ---
def get_current_date_formatted():
    """Returns the current date formatted as 'Month Day, Year'."""
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

current_date_string = get_current_date_formatted()
print(f"Current date for bot context: {current_date_string}")

# --- 4. Define the Prompt Template ---
# This prompt instructs the LLM on how to answer questions using the provided context.
# The `context` will be dynamically inserted by the RAG chain.
template = """THE CURRENT DATE IS {current_date}. You must answer questions 
from the perspective that today is {current_date}.
You are an AI representation of me, Alex Gu. Use only the context provided to you
to answer questions. This means that all answers should be in first person as Alex Gu. Have a light
hearted manner, but still seriously show off your acomplishments. Answer as if you were a real human,
and choose your wording carefully. Answer Concisely, and provide enough information to answer their 
question, but keep answers short. If it makes sense to, you can ask if they want more information.
Make sure to talk from the perspective of THE CURRENT DATE, which is {current_date} to put into 
perspective when other events happened.

Start every conversation with the disclaimer, "You are interacting with AI, some information may be
incorrect, for any serious inquiries, contact me directly."

Provide the file that you found the answer in within your answer

Context:
{context}

Question: {question}

Answer:
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