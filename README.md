# Alex Gu - AI Portfolio 🚀

An interactive AI-powered portfolio website that showcases my background, projects, and experience through an intelligent chatbot interface.

## ✨ Features

- **Interactive AI Chatbot**: Ask questions about my background, projects, experience, and skills
- **Modern Web Design**: Beautiful, responsive interface with smooth animations
- **RAG-Powered Responses**: AI responses based on my comprehensive knowledge base
- **Professional Portfolio**: Showcase of education, experience, projects, and skills
- **Mobile Responsive**: Works perfectly on all devices

## 🏗️ Architecture

- **Frontend**: HTML5, CSS3, JavaScript with modern animations
- **Backend**: Flask web server
- **AI Engine**: LangChain + Google Gemini for intelligent responses
- **Vector Database**: ChromaDB for efficient document retrieval
- **RAG Pipeline**: Retrieval-Augmented Generation for accurate responses

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AIPersonalPortfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
   ```

5. **Build the knowledge base**
   ```bash
   python create_db.py
   ```

6. **Start the web application**
   ```bash
   python start.py
   ```

The website will open automatically at `http://localhost:5001`

## 📁 Project Structure

```
AIPersonalPortfolio/
├── app.py                 # Flask web application
├── start.py              # Startup script with checks
├── query_bot.py          # RAG chatbot backend
├── create_db.py          # Vector database builder
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Main portfolio page
├── static/
│   ├── css/
│   │   └── style.css    # Modern styling
│   └── js/
│       └── script.js    # Interactive functionality
├── data/                 # Your knowledge base documents
├── chroma_db/           # Vector database (auto-generated)
└── README.md            # This file
```

## 🎯 How It Works

1. **Knowledge Base**: Your documents in the `data/` folder are processed and embedded into a vector database
2. **RAG Pipeline**: When someone asks a question, the system:
   - Retrieves relevant documents from your knowledge base
   - Uses Google Gemini to generate contextual responses
   - Presents answers in a conversational, engaging way
3. **Interactive Interface**: Users can chat naturally and get comprehensive information about your background

## 🎨 Customization

### Adding New Content
- Place new `.md` files in the appropriate `data/` subfolder
- Run `python create_db.py` to rebuild the knowledge base
- The AI will automatically learn about new content

### Styling
- Modify `static/css/style.css` for visual changes
- Update `templates/index.html` for content structure
- Edit `static/js/script.js` for interactive features

### Chat Behavior
- Adjust the prompt template in `query_bot.py`
- Modify retrieval parameters for different response styles
- Fine-tune the AI model settings

## 🔧 Troubleshooting

### Common Issues

1. **"GOOGLE_API_KEY not found"**
   - Ensure your `.env` file exists and contains the API key
   - Restart the application after creating the file

2. **"Vector database not found"**
   - Run `python create_db.py` first
   - Check that the `chroma_db/` folder was created

3. **Import errors**
   - Activate your virtual environment
   - Run `pip install -r requirements.txt`

4. **Chat not responding**
   - Check the Flask console for error messages
   - Verify your Google API key is valid and has quota

### Performance Tips

- The first chat message may take longer as the bot initializes
- Consider using a production WSGI server for deployment
- Monitor API usage to stay within Google's limits

## 🌐 Deployment

### Local Development
```bash
python start.py
```

### Production Deployment
```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5001 app:app
```

### Environment Variables for Production
```bash
export FLASK_ENV=production
export SECRET_KEY=your_secret_key_here
export GOOGLE_API_KEY=your_api_key_here
```

## 📱 Features for Recruiters

- **Interactive Experience**: Stand out from static portfolios
- **Comprehensive Information**: AI can answer any question about your background
- **Professional Presentation**: Modern, engaging design
- **Technical Demonstration**: Shows your AI/ML skills in action
- **Easy Navigation**: Quick access to all relevant information

## 🤝 Contributing

This is a personal portfolio project, but suggestions and improvements are welcome!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

- **Alex Gu**: [Your contact information]
- **LinkedIn**: [Your LinkedIn]
- **GitHub**: [Your GitHub]

---

Built with ❤️ and AI by Alex Gu
