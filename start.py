#!/usr/bin/env python3
"""
Startup script for Alex's AI Portfolio Web Application
"""

import os
import sys
import subprocess
import webbrowser
import time

def check_dependencies():
    """Check if required packages are installed."""
    try:
        import flask
        import langchain
        import chromadb
        print("✅ All required packages are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists with API key."""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please create a .env file with your GOOGLE_API_KEY")
        return False
    
    # Check if API key is set
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv('GOOGLE_API_KEY'):
        print("❌ GOOGLE_API_KEY not found in .env file!")
        print("Please add: GOOGLE_API_KEY=your_api_key_here")
        return False
    
    print("✅ Environment variables configured!")
    return True

def check_database():
    """Check if the vector database exists."""
    if not os.path.exists('./chroma_db'):
        print("❌ Vector database not found!")
        print("Please run: python create_db.py")
        return False
    
    print("✅ Vector database found!")
    return True

def start_app():
    """Start the Flask application."""
    print("\n🚀 Starting Alex's AI Portfolio...")
    print("=" * 50)
    
    # Check all prerequisites
    if not all([check_dependencies(), check_env_file(), check_database()]):
        print("\n❌ Please fix the issues above before starting the app.")
        return
    
    print("\n✅ All checks passed! Starting the web application...")
    
    # Start the Flask app
    try:
        from app import app
        print("🌐 Opening browser in 3 seconds...")
        time.sleep(3)
        webbrowser.open('http://localhost:5001')
        
        print("🔥 Flask app is running at: http://localhost:5001")
        print("📱 Press Ctrl+C to stop the server")
        print("=" * 50)
        
        app.run(debug=True, host='0.0.0.0', port=5001)
        
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        print("Please check the error message above.")

if __name__ == "__main__":
    start_app()
