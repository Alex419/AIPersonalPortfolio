from flask import Flask, render_template, request, jsonify
import os
from pathlib import Path

app = Flask(__name__)

# Check if we should use simple mode
# Default to simple mode (can be overridden with USE_SIMPLE_MODE=false)
USE_SIMPLE_MODE = os.environ.get('USE_SIMPLE_MODE', 'true').lower() == 'true'

# Log the mode for debugging
print(f"USE_SIMPLE_MODE environment variable: {os.environ.get('USE_SIMPLE_MODE', 'not set (defaulting to true)')}")
print(f"Using simple mode: {USE_SIMPLE_MODE}")

# Initialize the bot only if not in simple mode
bot = None
if not USE_SIMPLE_MODE:
    try:
        from query_bot import AlexGuBot
        bot = AlexGuBot()
        print("RAG bot initialized successfully")
    except Exception as e:
        print(f"Warning: Could not initialize bot: {e}")
        print("Falling back to simple mode")
        USE_SIMPLE_MODE = True
else:
    print("Simple mode enabled - skipping RAG bot initialization")

# Data directory path
DATA_DIR = Path(__file__).parent / 'data'

def format_display_name(filename):
    """Convert filename to a nicely formatted display name"""
    import re
    
    # Remove extension if present
    name = filename.replace('.md', '')
    
    # Replace underscores and hyphens with spaces
    name = name.replace('_', ' ').replace('-', ' ')
    
    # Remove any existing spaces and rebuild
    name = name.replace(' ', '')
    
    # Split camelCase and handle acronyms intelligently
    # Insert spaces at word boundaries:
    # 1. Before capital letters that follow lowercase/digit (camelCase)
    # 2. After acronyms (all caps) when followed by a capital letter starting a lowercase word
    # 3. Before capital letters that are part of a new word after an acronym
    
    # First pass: split lowercase/digit followed by uppercase
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', name)
    
    # Second pass: split acronym (2+ uppercase) followed by uppercase that starts a lowercase word
    # This handles "MITMedia" -> "MIT Media"
    name = re.sub(r'([A-Z]{2,})([A-Z][a-z])', r'\1 \2', name)
    
    # Split into words and format
    words = name.split()
    formatted_words = []
    
    for word in words:
        word = word.strip()
        if not word:
            continue
            
        # If it's all caps and 2+ letters (acronym), keep it as is
        if word.isupper() and len(word) >= 2:
            formatted_words.append(word)
        # Otherwise, capitalize first letter, rest lowercase
        else:
            formatted_words.append(word.capitalize())
    
    return ' '.join(formatted_words)

@app.route('/')
def index():
    if USE_SIMPLE_MODE:
        return render_template('index_simple.html')
    else:
        return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if USE_SIMPLE_MODE:
        return jsonify({'error': 'Chat is disabled in simple mode'}), 503
    
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        if not bot:
            return jsonify({'error': 'Bot not initialized'}), 500
        
        # Get response from the bot
        response = bot.query(message)
        
        return jsonify({'response': response})
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/category/<category>')
def get_category_files(category):
    """Get list of files in a category"""
    try:
        category_path = DATA_DIR / category
        
        if not category_path.exists() or not category_path.is_dir():
            return jsonify({'error': 'Category not found'}), 404
        
        files = []
        for file_path in sorted(category_path.glob('*.md')):
            # Get display name (filename without extension, formatted nicely)
            filename = file_path.name
            display_name = format_display_name(filename)
            
            # Read first few lines for preview
            preview = ""
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()[:3]
                    preview = ' '.join(line.strip() for line in lines if line.strip())
                    if len(preview) > 150:
                        preview = preview[:150] + '...'
            except:
                pass
            
            files.append({
                'filename': file_path.name,
                'displayName': display_name,
                'preview': preview
            })
        
        return jsonify({'files': files})
    
    except Exception as e:
        print(f"Error loading category {category}: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/content/<category>/<filename>')
def get_content(category, filename):
    """Get content of a specific file"""
    try:
        file_path = DATA_DIR / category / filename
        
        # Security check: ensure file is within data directory
        if not str(file_path).startswith(str(DATA_DIR)):
            return jsonify({'error': 'Invalid path'}), 400
        
        if not file_path.exists() or not file_path.is_file():
            return jsonify({'error': 'File not found'}), 404
        
        # Only allow .md files
        if not filename.endswith('.md'):
            return jsonify({'error': 'Invalid file type'}), 400
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return jsonify({'content': content})
    
    except Exception as e:
        print(f"Error loading content {category}/{filename}: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Use environment variable for port, default to 5001 for local development
    port = int(os.environ.get('PORT', 5001))
    
    # Debug mode only in development
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
