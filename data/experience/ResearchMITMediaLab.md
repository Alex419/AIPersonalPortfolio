# Research Intern: Conversational AI for Loneliness Reduction at MIT Media Lab - Fluid Interfaces (May 2023 - September 2023)

During my internship at the MIT Media Lab's Fluid Interfaces group in Cambridge, MA, I developed a novel conversational AI system aimed at mitigating feelings of loneliness among older adults, particularly those experiencing memory impairments. This project combined advanced AI techniques with human-centered design to encourage social interaction.

## Project Goal & Vision
The core idea was to create an AI assistant that could transcribe and summarize voice memos, calls, and meetings. This system would allow individuals, especially those with memory impairments, to easily review past conversations, facilitating follow-up on previous topics and preventing repetitive discussions in future interactions. The broader premise was to address a significant factor contributing to loneliness in older adults: the embarrassment or hesitation to reach out due to memory recall difficulties. The lab's previous research underscored the severe impact of loneliness on this demographic.

## My Contributions & Technical Implementation
I was responsible for the end-to-end development of the core AI functionality and a supporting web application:
* **Conversational AI Development:**
    * Designed and implemented a Python application to process audio files, leveraging **OpenAI's Whisper engine** for accurate transcription. This included labeling transcripts with timestamps and speaker names.
    * Integrated a summarization feature to provide concise, bullet-point summaries of conversations, which could be easily recalled for future reference.
* **Web Application Development:**
    * Built a user-friendly web application from scratch using **JavaScript (React)** to serve as the front-end interface.
    * Enabled users to manage their conversation summaries and visualize interaction statistics.
* **User Research & Design:**
    * Collaborated directly with senior citizens from a nearby retirement home to gather crucial feedback and insights into their specific needs and pain points regarding memory recall and social engagement.
    * Designed the web application's infrastructure and features to directly address these user needs, specifically to promote social interaction and reduce social anxiety.

## Technical Challenges & Innovative Solutions
Throughout the project, I encountered several significant technical hurdles that required iterative problem-solving and adaptation:

### 1. Accent Recognition in Speech-to-Text
* **Challenge:** Initial attempts with certain Language Learning Models (LLMs) for transcription struggled significantly with diverse accents (e.g., a Russian accent), leading to incoherent and inaccurate transcripts.
* **Solution:** Migrated the transcription engine to **OpenAI's Whisper**, which demonstrated significantly superior accent recognition and overall transcription accuracy. This was a critical pivot for the project's viability.

### 2. Speaker Diarization
* **Challenge:** While Whisper offered high accuracy, it lacked native support for speaker diarization (identifying different speakers in a conversation and segmenting their turns). This was crucial for summarizing conversations accurately and attributing dialogue.
* **Solution:** Developed a custom pipeline by integrating **`pydub`** (for audio manipulation) with a dedicated speaker diarization model. This involved:
    * Using the speaker diarization pipeline to identify turn-taking points and generate timestamps.
    * Breaking down the original audio into segments based on these timestamps.
    * Running each audio segment through Whisper for accurate transcription.
    * Modified the segmentation logic and incorporated sound clip analysis to precisely identify segment breaks, even in challenging audio.
    * Devised a method to combine consecutive sentences spoken by the same person, improving transcript readability by presenting dialogue in coherent blocks rather than fragmented sentences.

### 3. Handling Various Audio Formats & Quality
* **Challenge:** The system needed to ingest various audio file types (e.g., MP3) while maintaining high-quality transcription.
* **Solution:** Utilized **FFmpeg** to convert diverse audio file formats into WAV files, ensuring consistent, high-fidelity input for the speech recognition pipeline.

## Future Vision & Broader Impact
My work laid the groundwork for future expansions, including:
* Recommending individuals for users to connect with based on conversation history or last contact.
* Extracting dates from transcripts to suggest events for Google Calendar or other calendar services.
* The application's core concept of enhancing memory and encouraging social interaction holds significant potential beyond older adults, offering benefits to a broader population, including personal productivity and relationship management.

## Technologies Used
* **Languages:** Python, JavaScript (React)
* **AI/ML Models & APIs:** OpenAI (Whisper API), Google Speech Recognition API (for initial exploration)
* **Audio Processing:** `pydub`, FFmpeg
* **Development Tools:** Git/GitHub

## Skills Developed
* **AI/ML:** Conversational AI Design, Speech-to-Text (Transcription), Summarization, Speaker Diarization.
* **Software Development:** Full-stack development (Python backend, React frontend), API Integration, Data Processing, Prototype Development.
* **Research & Design:** User Research (survey design, feedback gathering), Human-Centered Design, Problem Identification.
* **Problem-Solving:** Iterative debugging, selecting appropriate technologies, custom pipeline development, overcoming limitations of existing APIs.
* **Communication:** Collaborating with diverse stakeholders (senior citizens, lab researchers).
* **Adaptability:** Quickly learning and integrating new tools and adapting to evolving project requirements.