import os
from dotenv import load_dotenv
import datetime
from typing import List, Dict, Any

# LangChain components for RAG
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

class AlexGuBot:
    def __init__(self):
        """Initialize the Alex Gu portfolio bot."""
        self.setup_config()
        self.setup_models()
        self.setup_vector_store()
        self.setup_retriever()
        self.setup_rag_chain()

    def setup_config(self):
        """Load configuration and API keys."""
        load_dotenv()
        
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file. Please set it.")
        
        self.persist_directory = "./chroma_db"
        self.current_date = datetime.date.today().strftime("%B %d, %Y")
        print(f"🤖 Alex Gu Bot initialized for {self.current_date}")

    def setup_models(self):
        """Initialize the embeddings and LLM models."""
        self.embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        print("✓ Initialized Google Gemini Embeddings model")
        
        # Use the latest Gemini model with optimized settings
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",  # Latest model
            google_api_key=self.google_api_key,
            temperature=0.3,  # Lower temperature for more consistent responses
            max_output_tokens=2000  # Reasonable limit for portfolio responses
        )
        print("✓ Initialized Google Gemini LLM")

    def setup_vector_store(self):
        """Load the existing vector store."""
        print(f"📂 Loading ChromaDB vector store from '{self.persist_directory}'...")
        
        if not os.path.exists(self.persist_directory):
            raise FileNotFoundError(f"Vector store not found at {self.persist_directory}. Please run create_db.py first.")
        
        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings_model
        )
        print("✓ ChromaDB vector store loaded successfully")

    def smart_retriever(self, query: str) -> List[Document]:
        """
        Smart retrieval that adjusts based on query type and uses multiple strategies.
        """
        # Determine query type and adjust retrieval strategy
        query_lower = query.lower()
        
        # For overview/summary questions, prioritize overview documents
        if any(word in query_lower for word in ['overview', 'summary', 'about', 'tell me about', 'who is', 'introduction']):
            k = 6  # Get more context for overview questions
            search_type = "mmr"  # Maximal Marginal Relevance for diversity
        # For specific technical questions, be more precise
        elif any(word in query_lower for word in ['project', 'experience', 'skill', 'technology', 'work']):
            k = 4
            search_type = "similarity"
        else:
            k = 4
            search_type = "similarity"
        
        # Retrieve documents
        retriever = self.vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={"k": k}
        )
        
        docs = retriever.invoke(query)
        
        # Rerank results based on query type and document category
        scored_docs = []
        for doc in docs:
            score = 1.0  # Base score
            category = doc.metadata.get('category', 'general')
            
            # Boost scores for relevant categories based on query
            if 'project' in query_lower and category == 'projects':
                score += 0.5
            elif any(word in query_lower for word in ['experience', 'work', 'job']) and category == 'experience':
                score += 0.5
            elif 'education' in query_lower and category == 'education':
                score += 0.5
            elif 'leadership' in query_lower and category == 'leadership':
                score += 0.5
            elif any(word in query_lower for word in ['overview', 'about', 'summary']) and category == 'overview':
                score += 1.0  # Strong boost for overview questions
            
            scored_docs.append((score, doc))
        
        # Sort by score and return top documents
        scored_docs.sort(reverse=True, key=lambda x: x[0])
        return [doc for _, doc in scored_docs]

    def setup_retriever(self):
        """Setup the document retriever."""
        print("🔍 Retriever set up with smart retrieval strategy")

    def format_context(self, docs: List[Document]) -> str:
        """Format retrieved documents into context string."""
        if not docs:
            return "No relevant information found."
        
        context_parts = []
        for i, doc in enumerate(docs, 1):
            source = os.path.basename(doc.metadata.get('source', 'Unknown'))
            category = doc.metadata.get('category', 'general')
            
            context_parts.append(
                f"[Document {i} - {source} ({category})]:\n{doc.page_content}\n"
            )
        
        return "\n".join(context_parts)

    def setup_rag_chain(self):
        """Setup the complete RAG chain."""
        
        # Improved prompt template
        template = """You are Alex Gu, speaking from the perspective of {current_date}.

**Your Persona:**
- Confident but approachable professional
- Passionate about AI, machine learning, and technology
- Easy-going with a good sense of humor, but serious about work
- Focus on technical projects and AI experience first
- Speak naturally in first person ("I", "my", "we")

**Response Guidelines:**
1. **Accuracy First**: Only use information from the provided context. Never invent details.
2. **Perspective**: Speak as if it's {current_date}. Reference past events in past tense with proper context.
3. **Prioritization**: 
   - For broad questions: Use overview documents and synthesize across experiences
   - For specific questions: Focus on detailed project/experience information
4. **Format**: Keep responses conversational but professional. End with an invitation to learn more.
5. **Clarity**: If the question is vague, politely ask for clarification about which aspect they'd like to know more about.

**Context Information:**
{context}

**Question:** {question}

**Response as Alex:**
"""

        self.prompt = ChatPromptTemplate.from_template(template)
        
        # Create the RAG chain
        self.rag_chain = (
            {
                "context": RunnableLambda(lambda x: self.format_context(self.smart_retriever(x))),
                "question": RunnablePassthrough(),
                "current_date": RunnableLambda(lambda x: self.current_date)
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        
        print("✓ RAG chain assembled with improved context formatting")

    def query(self, question: str) -> str:
        """Process a single query and return the response."""
        try:
            response = self.rag_chain.invoke(question)
            return response
        except Exception as e:
            return f"I apologize, but I encountered an error: {e}. Please try rephrasing your question."

    def chat(self):
        """Start interactive chat session."""
        print("\n" + "="*50)
        print("🤖 Alex Gu Portfolio Bot")
        print("="*50)
        print("Hi! I'm Alex's AI assistant. Ask me anything about Alex's background,")
        print("projects, experience, or skills. Type 'bye' to exit.")
        print("="*50)

        while True:
            try:
                user_query = input("\n💬 Your question: ").strip()
                
                if user_query.lower() in ['bye', 'exit', 'quit']:
                    print("\n👋 Thanks for chatting! Feel free to reach out to Alex directly for more detailed discussions.")
                    break
                
                if not user_query:
                    print("Please ask a question about Alex's background, projects, or experience.")
                    continue

                print("\n🤔 Let me think about that...")
                response = self.query(user_query)
                print(f"\n🤖 Alex: {response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Chat ended. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                print("Please try again or contact Alex directly.")

def main():
    """Main function to run the bot."""
    try:
        bot = AlexGuBot()
        bot.chat()
    except Exception as e:
        print(f"❌ Failed to initialize bot: {e}")
        print("Make sure you've run create_db.py first and have your GOOGLE_API_KEY set.")

if __name__ == "__main__":
    main()