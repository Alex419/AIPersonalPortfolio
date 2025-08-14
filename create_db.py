import os
import re
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

class AlexPortfolioDBBuilder:
    def __init__(self):
        """Initialize the database builder for Alex's portfolio documents."""
        load_dotenv()
        self.embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.persist_directory = "./chroma_db"
        
    def load_and_categorize_documents(self):
        """Load documents and categorize them based on structure and content."""
        print("📁 Loading documents from ./data/...")
        
        loader = DirectoryLoader(
            './data',
            glob="**/*.md",
            loader_cls=TextLoader
        )
        
        documents = loader.load()
        
        if not documents:
            print("❌ No documents found in the 'data' directory.")
            exit()
        
        print(f"✓ Loaded {len(documents)} document(s)")
        
        # Categorize and enhance documents
        categorized_docs = []
        for doc in documents:
            enhanced_doc = self._enhance_document_metadata(doc)
            categorized_docs.append(enhanced_doc)
            
        return categorized_docs
    
    def _enhance_document_metadata(self, doc: Document) -> Document:
        """Enhanced metadata extraction for Alex's document structure."""
        filepath = doc.metadata['source']
        filename = os.path.basename(filepath)
        directory_path = os.path.dirname(filepath)
        
        # Extract category from directory structure
        path_parts = directory_path.lower().split(os.sep)
        
        # Determine main category
        if 'projects' in path_parts or 'project' in path_parts:
            category = 'projects'
        elif 'experience' in path_parts or 'work' in path_parts:
            category = 'experience'
        elif 'education' in path_parts or 'school' in path_parts:
            category = 'education'
        elif 'leadership' in path_parts:
            category = 'leadership'
        elif 'hobbies' in path_parts or 'interests' in path_parts:
            category = 'hobbies'
        else:
            category = 'general'
        
        # Determine document type (overview vs detailed)
        is_overview = 'overview' in filename.lower()
        
        # Extract title from content (first header)
        title = self._extract_title_from_content(doc.page_content)
        
        # Extract time information from content
        time_info = self._extract_time_information(doc.page_content)
        
        # Enhanced metadata
        doc.metadata.update({
            'category': category,
            'is_overview': is_overview,
            'document_type': 'overview' if is_overview else 'detailed',
            'title': title,
            'filename': filename,
            'directory': os.path.dirname(filepath),
            'content_length': len(doc.page_content),
            'priority_score': self._calculate_priority_score(doc.page_content, is_overview, category),
            'time_period': time_info['period'],
            'year': time_info['year'],
            'season': time_info['season'],
            'is_recent': time_info['is_recent']
        })
        
        return doc
    
    def _extract_time_information(self, content: str) -> dict:
        """Extract time information from document content."""
        content_lower = content.lower()
        
        # Default values
        time_info = {
            'period': 'unknown',
            'year': None,
            'season': None,
            'is_recent': False
        }
        
        # Extract years (2020-2025)
        import re
        year_matches = re.findall(r'\b(202[0-5])\b', content)
        if year_matches:
            time_info['year'] = int(max(year_matches))  # Most recent year
        
        # Extract seasons
        seasons = ['summer', 'fall', 'spring', 'winter']
        for season in seasons:
            if season in content_lower:
                time_info['season'] = season
                break
        
        # Determine if recent (2024-2025)
        if time_info['year'] and time_info['year'] >= 2024:
            time_info['is_recent'] = True
        
        # Create period string
        if time_info['season'] and time_info['year']:
            time_info['period'] = f"{time_info['season']} {time_info['year']}"
        elif time_info['year']:
            time_info['period'] = str(time_info['year'])
        elif time_info['season']:
            time_info['period'] = time_info['season']
        
        # Check for specific time indicators
        if 'summer 2025' in content_lower:
            time_info.update({
                'period': 'summer 2025',
                'year': 2025,
                'season': 'summer',
                'is_recent': True
            })
        
        return time_info
    
    def _extract_title_from_content(self, content: str) -> str:
        """Extract title from markdown content."""
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
            elif line.startswith('## ') and not line.startswith('### '):
                return line[3:].strip()
        return "Untitled"
        """Calculate priority score for document ranking."""
        score = 1.0
        
        # Overview documents get higher priority for general queries
        if is_overview:
            score += 2.0
        
        # Boost certain categories
        if category in ['projects', 'experience']:
            score += 0.5
        
        # Boost documents with key technical terms
        technical_terms = ['AI', 'ML', 'machine learning', 'python', 'react', 'API', 'database']
        for term in technical_terms:
            if term.lower() in content.lower():
                score += 0.1
        
        return score
    
    def create_specialized_chunks(self, documents):
        """Create chunks optimized for Alex's document structure."""
        print("✂️  Creating specialized chunks...")
        
        all_chunks = []
        
        for doc in documents:
            if doc.metadata['is_overview']:
                # Overview documents: Smaller chunks for precision
                chunks = self._chunk_overview_document(doc)
            else:
                # Detailed documents: Larger chunks for context
                chunks = self._chunk_detailed_document(doc)
            
            all_chunks.extend(chunks)
        
        print(f"✓ Created {len(all_chunks)} specialized chunks")
        return all_chunks
    
    def _chunk_overview_document(self, doc: Document):
        """Chunk overview documents with smaller, precise chunks."""
        # Overview documents should be chunked by bullet points/sections
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,  # Smaller for overview precision
            chunk_overlap=50,
            length_function=len,
            add_start_index=True,
            separators=[
                "\n\n* ",    # Bullet points in overviews
                "\n* ",      # Bullet points
                "\n\n",      # Paragraphs
                "\n",        # Lines
                ". ",        # Sentences
                " ",         # Words
                ""           # Characters
            ]
        )
        
        chunks = text_splitter.split_documents([doc])
        
        # Add special metadata for overview chunks
        for chunk in chunks:
            chunk.metadata['chunk_type'] = 'overview'
            chunk.metadata['search_priority'] = 'high'
        
        return chunks
    
    def _chunk_detailed_document(self, doc: Document):
        """Chunk detailed documents with larger, contextual chunks."""
        # For detailed docs, preserve larger context
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=900,  # Larger for detailed context
            chunk_overlap=150,
            length_function=len,
            add_start_index=True,
            separators=[
                "\n## ",     # Major sections
                "\n### ",    # Subsections
                "\n\n",      # Paragraphs
                "\n",        # Lines
                ". ",        # Sentences
                " ",         # Words
                ""           # Characters
            ]
        )
        
        chunks = text_splitter.split_documents([doc])
        
        # Add metadata for detailed chunks
        for chunk in chunks:
            chunk.metadata['chunk_type'] = 'detailed'
            chunk.metadata['search_priority'] = 'medium'
        
        return chunks
    
    def create_synthetic_summary_chunks(self, documents):
        """Create synthetic summary chunks for better high-level queries."""
        print("🔄 Creating synthetic summary chunks...")
        
        synthetic_chunks = []
        
        # Group documents by category
        categories = {}
        for doc in documents:
            cat = doc.metadata['category']
            if cat not in categories:
                categories[cat] = {'overview': [], 'detailed': []}
            
            if doc.metadata['is_overview']:
                categories[cat]['overview'].append(doc)
            else:
                categories[cat]['detailed'].append(doc)
        
        # Create category summaries
        for category, docs in categories.items():
            if docs['overview']:  # Only if we have overview docs
                summary_content = f"# {category.title()} Summary\n\n"
                
                for doc in docs['overview']:
                    title = doc.metadata['title']
                    # Extract key bullet points
                    content_preview = self._extract_key_points(doc.page_content)
                    summary_content += f"## {title}\n{content_preview}\n\n"
                
                # Create synthetic document
                synthetic_doc = Document(
                    page_content=summary_content,
                    metadata={
                        'source': f'synthetic_{category}_summary',
                        'category': category,
                        'is_overview': True,
                        'document_type': 'synthetic_summary',
                        'title': f'{category.title()} Summary',
                        'filename': f'{category}_summary.md',
                        'synthetic': True,
                        'priority_score': 3.0,  # High priority for summaries
                        'chunk_type': 'summary',
                        'search_priority': 'highest'
                    }
                )
                
                synthetic_chunks.append(synthetic_doc)
        
        print(f"✓ Created {len(synthetic_chunks)} synthetic summary chunks")
        return synthetic_chunks
    
    def _extract_key_points(self, content: str, max_points: int = 3) -> str:
        """Extract key bullet points from content."""
        lines = content.split('\n')
        key_points = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('* ') and len(key_points) < max_points:
                key_points.append(line)
        
        return '\n'.join(key_points) if key_points else content[:200] + "..."
    
    def build_database(self):
        """Main method to build the optimized database."""
        print("\n🚀 Building Alex's Portfolio Database")
        print("=" * 50)
        
        # Step 1: Load and categorize documents
        documents = self.load_and_categorize_documents()
        
        # Step 2: Create specialized chunks
        chunks = self.create_specialized_chunks(documents)
        
        # Step 3: Create synthetic summaries
        synthetic_chunks = self.create_synthetic_summary_chunks(documents)
        
        # Step 4: Combine all chunks
        all_chunks = chunks + synthetic_chunks
        
        # Step 5: Remove existing database
        if os.path.exists(self.persist_directory):
            import shutil
            shutil.rmtree(self.persist_directory)
            print("🗑️  Removed existing vector store")
        
        # Step 6: Create vector store
        print("🔄 Creating optimized ChromaDB vector store...")
        vector_store = Chroma.from_documents(
            documents=all_chunks,
            embedding=self.embeddings_model,
            persist_directory=self.persist_directory
        )
        
        print(f"✅ Database created with {len(all_chunks)} total chunks")
        
        # Step 7: Test the database
        self._test_database(vector_store)
        
        return vector_store
    
    def _test_database(self, vector_store):
        """Test the database with sample queries."""
        print("\n🧪 Testing database with sample queries...")
        
        test_queries = [
            "What projects has Alex worked on?",
            "Tell me about Alex's AI experience",
            "What is the DJ Transition Analysis project?",
            "What leadership experience does Alex have?"
        ]
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n  Test {i}: {query}")
            retriever = vector_store.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 3}
            )
            results = retriever.invoke(query)
            
            for j, doc in enumerate(results, 1):
                doc_type = doc.metadata.get('document_type', 'unknown')
                category = doc.metadata.get('category', 'unknown')
                title = doc.metadata.get('title', 'untitled')
                priority = doc.metadata.get('search_priority', 'unknown')
                
                print(f"    {j}. [{doc_type}] {title} ({category}) - Priority: {priority}")
                print(f"       Preview: {doc.page_content[:100]}...")

def main():
    """Main function to build the database."""
    try:
        builder = AlexPortfolioDBBuilder()
        builder.build_database()
        print("\n✅ Database build complete! Ready for queries.")
    except Exception as e:
        print(f"❌ Error building database: {e}")
        raise

if __name__ == "__main__":
    main()