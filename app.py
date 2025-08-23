from flask import Flask, render_template, request, jsonify, session
import os
from dotenv import load_dotenv
from query_bot import AlexGuBot
import uuid

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Initialize the bot (will be done on first request)
bot = None

def get_bot():
    """Initialize bot on first use to avoid startup delays."""
    global bot
    if bot is None:
        try:
            bot = AlexGuBot()
        except Exception as e:
            print(f"Error initializing bot: {e}")
            return None
    return bot

@app.route('/')
def index():
    """Main portfolio page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages from the frontend."""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get bot instance
        bot_instance = get_bot()
        if bot_instance is None:
            return jsonify({'error': 'Bot is not available. Please try again later.'}), 500
        
        # Process the message
        response = bot_instance.query(message)
        
        # Generate a unique message ID for the frontend
        message_id = str(uuid.uuid4())
        
        return jsonify({
            'response': response,
            'message_id': message_id,
            'timestamp': 'now'
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'An error occurred while processing your message.'}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'bot_available': get_bot() is not None})

if __name__ == '__main__':
    # Check if bot can be initialized
    try:
        test_bot = get_bot()
        if test_bot:
            print("✅ Bot initialized successfully!")
        else:
            print("⚠️  Bot initialization failed")
    except Exception as e:
        print(f"❌ Bot initialization error: {e}")
    
    app.run(debug=True, host='0.0.0.0', port=5001)
