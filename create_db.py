import os
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
print("Using Google Gemini Embeddings.")

print("Loading documents from ./data/...")
loader = DirectoryLoader(
    './data',
    glob="**/*.md",
    loader_cls=TextLoader
)

documents = loader.load()

if not documents:
    print("No documents found in the 'data' directory. Please check the path and file extensions.")
    exit()

print(f"Loaded {len(documents)} document(s).")

# --- Text Splitting (as before) ---
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=750,
    chunk_overlap=150,
    length_function=len,
    add_start_index=True,
)
chunks = text_splitter.split_documents(documents)
print(f"Split into {len(chunks)} chunks.")

# --- Vector Store Creation and Persistence ---
print("Creating/updating ChromaDB vector store...")
PERSIST_DIRECTORY = "./chroma_db"

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings_model, # Use the Gemini embeddings model
    persist_directory=PERSIST_DIRECTORY
)

print(f"ChromaDB vector store created and persisted to '{PERSIST_DIRECTORY}'.")
print("Database setup complete. You can now use this vector store for RAG queries.")