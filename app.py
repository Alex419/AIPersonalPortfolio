from flask import Flask, render_template, request, jsonify
from query_bot import AlexGuBot
import os

app = Flask(__name__)

# Initialize the bot
bot = AlexGuBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from the bot
        response = bot.query(message)
        
        return jsonify({'response': response})
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Use environment variable for port, default to 5001 for local development
    port = int(os.environ.get('PORT', 5001))
    
    # Debug mode only in development
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
