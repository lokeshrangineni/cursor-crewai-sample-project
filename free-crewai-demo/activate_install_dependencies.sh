#!/bin/bash
# Conda Environment Setup for FREE CrewAI Demo
# Creates and activates: crewai-free-demo

set -e  # Exit on any error

CONDA_ENV_NAME="crewai-free-demo"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🆓 FREE CrewAI Demo - Conda Environment Setup"
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

# Check if environment already exists
if conda env list | grep -q "^$CONDA_ENV_NAME "; then
    echo "✅ Environment '$CONDA_ENV_NAME' already exists"
    echo "🔄 Updating environment from environment.yml..."
    conda env update -n "$CONDA_ENV_NAME" -f environment.yml
else
    echo "📦 Creating conda environment from environment.yml..."
    conda env create -f environment.yml
    echo "✅ Environment created successfully"
fi

# Activate environment
echo ""
echo "🔄 Activating environment: $CONDA_ENV_NAME"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV_NAME"

if [[ "$CONDA_DEFAULT_ENV" == "$CONDA_ENV_NAME" ]]; then
    echo "✅ Environment activated: $CONDA_DEFAULT_ENV"
else
    echo "❌ Failed to activate environment"
    exit 1
fi

# Dependencies are already installed via conda environment.yml
echo ""
echo "✅ Dependencies installed via conda environment"

# Check if Ollama is installed
echo ""
echo "🔍 Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed: $(ollama --version 2>/dev/null || echo 'version unknown')"
    
    # Check if model is available
    if ollama list | grep -q "llama3.2:3b"; then
        echo "✅ Llama 3.2 3B model is ready"
        MODEL_READY=true
    else
        echo "⚠️  Llama 3.2 3B model not found"
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
    echo "🤖 AI Model: Ready (Llama 3.2 3B)"
    echo ""
    echo "🚀 Ready to run FREE demo:"
    echo "   python crewai_free_demo.py"
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