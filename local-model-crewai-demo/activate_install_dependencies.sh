#!/bin/bash
# Conda Environment Setup for Local Model CrewAI Demo
# Creates and activates: crewai-free-demo

set -e  # Exit on any error

CONDA_ENV_NAME="crewai-free-demo"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🏠 Local Model CrewAI Demo - Environment Setup"
echo "=============================================="
echo "Environment: $CONDA_ENV_NAME"
echo "Location: $SCRIPT_DIR"
echo ""

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Conda not found!"
    echo "Please install Anaconda or Miniconda:"
    echo "https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

echo "✅ Conda found: $(conda --version)"

echo ""
echo "🔧 Setting up conda environment: $CONDA_ENV_NAME"

# Check if environment already exists
if conda env list | grep -q "^$CONDA_ENV_NAME "; then
    echo "✅ Environment '$CONDA_ENV_NAME' already exists"
    echo "🔄 Updating environment..."
    
    # Update the environment
    conda env update -n $CONDA_ENV_NAME -f environment.yml --prune
    
    if [ $? -eq 0 ]; then
        echo "✅ Environment updated successfully"
    else
        echo "❌ Failed to update environment"
        exit 1
    fi
else
    echo "🆕 Creating new environment..."
    
    # Create new environment
    conda env create -f environment.yml
    
    if [ $? -eq 0 ]; then
        echo "✅ Environment created successfully"
    else
        echo "❌ Failed to create environment"
        exit 1
    fi
fi

echo ""
echo "🎯 Activating environment..."

# Activate the environment
conda activate $CONDA_ENV_NAME

if [ $? -eq 0 ]; then
    echo "✅ Environment activated: $CONDA_ENV_NAME"
else
    echo "❌ Failed to activate environment"
    echo "💡 Try manually: conda activate $CONDA_ENV_NAME"
    exit 1
fi

echo ""
echo "📦 Installing additional dependencies..."

# Install additional dependencies via pip
pip install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Check if Ollama is installed
echo ""
echo "🔍 Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed: $(ollama --version 2>/dev/null || echo 'version unknown')"
    
    # Check if model is available
    if ollama list | grep -q "mistral:latest"; then
        echo "✅ Mistral model is ready"
        MODEL_READY=true
    else
        echo "⚠️  Mistral model not found"
        MODEL_READY=false
    fi
else
    echo "⚠️  Ollama not installed"
    MODEL_READY=false
fi

echo ""
echo "🎉 Conda Environment Setup Complete!"
echo "====================================="
echo "🐍 Environment: $CONDA_ENV_NAME (Python $(python --version 2>&1 | cut -d' ' -f2))"
echo "📦 Dependencies: Installed"

if [[ "$MODEL_READY" == true ]]; then
    echo "🤖 AI Model: Ready (Mistral)"
    echo ""
    echo "🚀 Ready to run demo:"
    echo "   python crewai_free_demo.py      # Command line"
    echo "   streamlit run streamlit_app.py  # Web interface"
else
    echo "🤖 AI Model: Not ready"
    echo ""
    echo "🔧 Next steps:"
    echo "1. Run: ./setup_ollama.sh"
    echo "2. Then: python crewai_free_demo.py"
fi

echo ""
echo "💡 To activate this environment in the future:"
echo "   conda activate $CONDA_ENV_NAME"
echo ""
echo "🔍 To verify setup:"
echo "   conda list"
echo "   ollama list"

# Keep environment activated for user
echo ""
echo "✨ Environment '$CONDA_ENV_NAME' is now active and ready!"
echo "   Current shell will remain in this environment." 