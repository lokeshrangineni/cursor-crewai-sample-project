#!/bin/bash
# ONE-CLICK Setup for Local Model CrewAI Demo
# Installs Ollama + Mistral for completely free AI

echo "🏠 Local Model CrewAI Demo Setup"
echo "================================"
echo "Installing: Ollama + Mistral (100% Free)"
echo ""

# Detect platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PLATFORM="Linux"
else
    PLATFORM="Other"
fi

echo "🖥️  Platform: $PLATFORM"

# Install Ollama
echo ""
echo "📦 Step 1: Installing Ollama..."

if command -v ollama &> /dev/null; then
    echo "✅ Ollama already installed"
else
    if [[ "$PLATFORM" == "macOS" ]]; then
        if command -v brew &> /dev/null; then
            echo "Installing via Homebrew..."
            brew install ollama
        else
            echo "📋 Manual installation needed:"
            echo "1. Visit: https://ollama.com/download"
            echo "2. Download and install for macOS"
            echo "3. Re-run this script"
            exit 1
        fi
    elif [[ "$PLATFORM" == "Linux" ]]; then
        echo "Installing for Linux..."
        curl -fsSL https://ollama.com/install.sh | sh
    else
        echo "📋 Manual installation needed:"
        echo "1. Visit: https://ollama.com/download"
        echo "2. Download for your platform"
        echo "3. Re-run this script"
        exit 1
    fi
fi

# Start Ollama service
echo ""
echo "🚀 Step 2: Starting Ollama service..."
ollama serve > /dev/null 2>&1 &
OLLAMA_PID=$!
echo "Service started (PID: $OLLAMA_PID)"

# Wait for service to be ready
echo "⏳ Waiting for service to start..."
sleep 3

# Download the model
echo ""
echo "📥 Step 3: Downloading Mistral model..."
echo "⚠️  This is a 4GB download - may take 10-15 minutes"
echo ""

ollama pull mistral:latest

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Setup Complete!"
    echo "==================="
    echo "🤖 Model: Mistral (4GB)"
    echo "💰 Cost: $0.00 (FREE!)"
    echo "🔒 Privacy: Runs locally"
    echo ""
    echo "📋 Available models:"
    ollama list
    echo ""
    echo "🚀 Ready to run demos:"
    echo "   python crewai_free_demo.py      # Command line"
    echo "   streamlit run streamlit_app.py  # Web interface"
    echo ""
    echo "💡 Pro Tips:"
    echo "• First run may be slower (model loading)"
    echo "• Keep Ollama running in background"
    echo "• Use 'ollama ps' to see loaded models"
    
else
    echo ""
    echo "❌ Model download failed"
    echo "🔧 Try manually:"
    echo "1. ollama pull mistral:latest"
    echo "2. ollama list (to verify)"
    echo "3. python crewai_free_demo.py"
fi

echo ""
echo "📚 Learn more about Ollama: https://ollama.com" 