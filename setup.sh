#!/bin/bash

echo "🚀 Setting up Alex's AI Portfolio..."
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip3 found: $(pip3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "Please create a .env file with your GOOGLE_API_KEY:"
    echo "GOOGLE_API_KEY=your_actual_api_key_here"
    echo ""
    echo "You can create it manually or run:"
    echo "echo 'GOOGLE_API_KEY=your_key_here' > .env"
    echo ""
else
    echo "✅ .env file found"
fi

# Check if database exists
if [ ! -d "chroma_db" ]; then
    echo "⚠️  Vector database not found!"
    echo "Please run: python create_db.py"
    echo ""
else
    echo "✅ Vector database found"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Make sure your .env file contains GOOGLE_API_KEY"
echo "2. Run: python create_db.py (if database doesn't exist)"
echo "3. Run: python start.py"
echo ""
echo "The website will open automatically at http://localhost:5000"
echo ""
echo "Happy coding! 🚀"
