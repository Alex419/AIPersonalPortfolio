# AI-Powered Personal Portfolio: Building a "Digital Me" - (Summer 2025)

## Project Overview
The AI-Powered Personal Portfolio is an innovative web-based application designed to make how I present my professional and personal profile more interactive and interesting. Moving beyond a static resume or traditional website, this interactive platform leverages Artificial Intelligence (AI) and Retrieval Augmented Generation (RAG) to serve as a "digital me," capable of answering dynamic questions about my experiences, projects, skills, and aspirations. 

## The Vision: A Conversational "Digital Me"
The core idea originated from a desire to create a truly interactive and personalized portfolio experience. Instead of recruiters or hiring managers passively reading through documents, they can engage in a natural language conversation with an AI model trained on my comprehensive personal data. This allows for:

* **Dynamic Q&A:** Answering specific, nuanced questions that might not be covered in a standard resume (e.g., "What leadership opportunities have you had?", "Tell me about your AI coursework at Columbia," "Describe a challenge you faced during your MIT Media Lab research").
* **Real-time Information Retrieval:** Providing immediate, contextually relevant answers by drawing directly from my curated knowledge base.
* **Personalized Engagement:** Offering a more engaging and memorable experience, fostering a deeper understanding of my profile.
* **Scalability:** The ability to easily update and expand my personal knowledge base without requiring code changes to the core AI logic.

## Problem Formulation: Possible Limitations of Traditional Portfolios
Traditional portfolios, while essential, often present several limitations:
* **Static Nature:** Information is fixed, requiring manual updates and lacking dynamic interaction.
* **Information Overload:** Recruiters have limited time; finding specific details can be cumbersome.
* **Lack of Context:** Resumes provide bullet points, but rarely the full narrative, challenges, or learnings behind an experience.
* **Limited Personalization:** Cannot adapt to a recruiter's specific interests or questions.
* **Passive Experience:** Doesn't actively engage the user or demonstrate problem-solving in real-time.

## Solution Architecture: Retrieval Augmented Generation (RAG)
The heart of this AI-powered portfolio is a **Retrieval Augmented Generation (RAG)** system. RAG was chosen over traditional fine-tuning of a Large Language Model (LLM) for its superior factuality, updatability, and cost-effectiveness when dealing with a custom, evolving knowledge base.
The RAG pipeline consists of the following key components:
1.  **Knowledge Base (Your Personal Data):** My comprehensive personal and professional information (experiences, projects, education, skills, hobbies) is meticulously organized into structured Markdown files.
2.  **Embedding Model:** Converts text data (from the knowledge base and user queries) into high-dimensional numerical vectors (embeddings), capturing their semantic meaning.
3.  **Vector Database (ChromaDB):** Stores these embeddings and their associated text chunks, enabling efficient semantic similarity search.
4.  **Retriever:** Given a user's query, it performs a similarity search in the vector database to retrieve the most semantically relevant chunks of my personal data.
5.  **Large Language Model (LLM):** Receives the user's original query *augmented* with the retrieved context. Its role is to synthesize a coherent, natural language answer based *only* on the provided context.
6.  **Prompt Engineering:** Carefully crafted instructions guide the LLM on how to interpret the query, utilize the context, and format its response.
7.  **Text-to-Speech (TTS) Integration (Future/External):** To achieve a voice response, the LLM's text output will be fed into a separate TTS service capable of voice cloning.

## Key Design Decisions & Iterative Development Process
The development of this project was an iterative process, involving critical design decisions and continuous refinement.

### 1. Interactive Experience Flow
* **Three-Part Structure:** The user flow was designed with a clear beginning, middle, and end:
    * **Introduction:** Welcomes the user, explains the AI's purpose, and provides initial guidance.
    * **Main Q&A:** The core interactive chat interface where users ask questions.
    * **Conclusion:** A polite wrap-up with clear calls to action (e.g., links to LinkedIn, resume).

### 2. LLM and Embeddings Model Selection
* **Decision:** Opted for **Google Gemini's API (`gemini-2.5-flash-latest` for LLM and `models/embedding-001` for embeddings)**.
* **Rationale:** Chosen for its competitive pricing, strong multimodal capabilities (future-proofing), large context window, and Google's robust student programs and ecosystem. This aligns with my academic focus on AI.

### 3. Data Structuring for RAG Optimization
* **Initial Approach:** Began by organizing personal data into logical Markdown files (e.g., `projects/`, `experience/`, `education/`).
* **Key Iteration: "Overview" Files:** A crucial refinement was introducing "overview" Markdown files within each major folder (e.g., `projects/overview.md`, `education/overview.md`, `leadership_contributions/overview_leadership.md`).
    * **Purpose:** These files provide concise summaries and highlights of the detailed content within their respective folders.
    * **Benefit:** This dramatically improves retrieval for high-level questions (e.g., "What projects have you worked on?"), allowing the LLM to provide a quick, coherent overview. For more detailed follow-ups, the RAG system can then retrieve the granular files. This strategy optimizes both speed and depth of response.

### 4. Chunking Strategy
* **Method:** Utilized LangChain's `RecursiveCharacterTextSplitter`.
* **Tuning:** Experimented with `chunk_size` (e.g., 700 characters) and `chunk_overlap` (e.g., 150 characters) to ensure that semantically coherent units (like a full project description or a list of techniques) were captured within single or well-overlapping chunks. This was critical for accurate retrieval and preventing fragmented information.

### 5. Prompt Engineering
* **Iterative Refinement:** The system prompt was continuously refined to guide the LLM's behavior. Key instructions included:
    * **Factual Grounding:** "Use ONLY the following pieces of retrieved context."
    * **Handling Unknowns:** "If the answer is not contained in the provided context, politely state that you don't have enough information."
    * **Structured Output:** 
    * **Persona:** 

### 6. Real-time Context (Current Date)
* **Implementation:** Integrated Python's `datetime` module to dynamically inject the current date into the prompt.
* **Purpose:** Ensures the AI's responses are time-aware, preventing it from referencing outdated information based on its training data cutoff. Done in attempt to keep the immersion.

### 7. Voice Integration Strategy
* **Decision:** Opted for a separate, specialized Text-to-Speech (TTS) service (e.g., ElevenLabs) for custom voice cloning, rather than relying on the native TTS capabilities of the core LLM (Gemini). I want the bot to feel more like me, which I thought could be done through making it sound like me as well.
* **Rationale:** As of mid-2025, dedicated TTS services offer superior voice cloning quality and control over custom voice models. While LLMs are gaining native TTS, they often rely on pre-built voices and do not yet offer the high-fidelity custom voice cloning feature that is central to the "digital me" vision.

## Technical Implementation Highlights
* **Programming Language:** Python
* **Frameworks:** LangChain (for RAG orchestration, document loading, splitting, retrieval, and chaining).
* **API Keys Management:** `python-dotenv` for secure loading of API keys from a `.env` file.
* **Vector Database:** ChromaDB (for local persistence and efficient semantic search).
* **LLM & Embeddings Integration:** `langchain-google-genai` for seamless interaction with Google Gemini models.
* **File Handling:** `langchain_community.document_loaders.DirectoryLoader` and `TextLoader` for ingesting Markdown files.

## Data Normalization
* **Data Normalization (from Transcripts/Raw Data):** The process of taking raw, inconsistent data (like the unofficial transcript or messy research notes) and transforming it into clean, structured Markdown.
    * **Solution:** Manual curation and careful formatting of Markdown files with clear headings, bullet points, and consistent terminology. This highlights the importance of data preprocessing in RAG.

## Impact & Future Scope
This AI-Powered Personal Portfolio significantly elevates my professional presentation by offering a dynamic, intelligent, and personalized experience. It directly showcases my skills in:
* **Applied AI/ML:** Demonstrating practical RAG implementation.
* **Software Engineering:** Building a full-stack (implied) application with robust backend logic.
* **Problem-Solving:** Documenting the challenges and solutions in the development process.
* **Data Management:** Structuring and preparing complex personal data for AI consumption.
* **User Experience:** Designing an intuitive and engaging interaction.

### Future Enhancements:
* **Full Voice Integration:** Implementing the chosen TTS service (e.g., ElevenLabs) to enable real-time audio responses in my cloned voice.
* **Multimodal Input:** Expanding the system to accept image or audio queries (e.g., "What's happening in this project screenshot?").
* **Agentic Capabilities:** Allowing the AI to perform actions (e.g., "Open my GitHub repo for Project X").
* **Enhanced Memory:** Implementing more sophisticated conversational memory beyond single-turn queries.
* **Feedback Loop:** Incorporating a mechanism for users to provide feedback on AI responses, allowing for continuous model and data refinement.

This project stands as a testament to my ability to conceptualize, design, and implement advanced AI solutions, transforming a traditional personal portfolio into a living, interactive demonstration of my capabilities.