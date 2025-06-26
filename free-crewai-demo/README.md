# 🆓 FREE CrewAI Demo Project

**The complete guide to exploring CrewAI with 100% free local AI - no API keys required!**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-green.svg)](https://ollama.com/)
[![CrewAI](https://img.shields.io/badge/framework-CrewAI-orange.svg)](https://crewai.com/)

## 🎯 What This Project Offers

This project provides **two different ways** to explore CrewAI:

1. **🖥️ Command Line Demo** - Interactive terminal-based research workflow
2. **🌐 Web App Interface** - Beautiful Streamlit web interface

**All demos are:**
- ✅ **100% FREE** - No API keys, no billing, no hidden costs
- ✅ **Private** - All AI processing happens locally on your machine
- ✅ **Reliable** - No internet dependency after initial setup
- ✅ **Low Resource** - Works with 4GB+ RAM
- ✅ **High Quality** - Uses Mistral AI model (4GB)

## 🚀 Quick Start (Recommended)

### Step 1: One-Click Environment Setup
```bash
# Clone the repository (if not already done)
git clone <your-repo-url>
cd free-crewai-demo

# Make setup script executable and run it
chmod +x activate_install_dependencies.sh
source activate_install_dependencies.sh
```

### Step 2: Install AI Models (One-Time)
```bash
# Install Ollama and download Mistral model
chmod +x setup_ollama.sh
./setup_ollama.sh
```

### Step 3: Choose Your Demo

**Option A: Web Interface (Recommended)**
```bash
streamlit run streamlit_app.py
# Opens http://localhost:8501 in your browser
```

**Option B: Command Line Demo**
```bash
python crewai_free_demo.py
# Interactive topic-based research
```

## 📋 Available Demos

### 🌐 Web App Interface (`streamlit_app.py`)
**Best for: Interactive exploration and professional presentations**

- Beautiful web interface with real-time progress
- Enter any research topic and get professional reports
- Download markdown reports with YAML metadata
- System status monitoring and error handling
- Example topics and quick-start buttons

**Usage:**
```bash
conda activate crewai-free-demo
streamlit run streamlit_app.py
```

### 🖥️ Command Line Demo (`crewai_free_demo.py`)
**Best for: Developers and command-line users**

- Interactive topic input via terminal
- Two-agent workflow: Researcher + Writer
- Generates professional markdown reports
- Saves files with timestamp and topic name
- Flexible topic research on any subject

**Usage:**
```bash
conda activate crewai-free-demo
python crewai_free_demo.py
```

## 🛠️ Manual Setup (If Automatic Setup Fails)

### Prerequisites
- **Python 3.11+** and **Conda/Miniconda**
- **4GB+ RAM** (8GB recommended)
- **5GB+ disk space** (for models and dependencies)
- **macOS, Linux, or Windows with WSL**

### Step-by-Step Manual Setup

1. **Create Conda Environment**
```bash
conda create -n crewai-free-demo python=3.11 -y
conda activate crewai-free-demo
```

2. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

3. **Install Ollama**
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows
# Download from https://ollama.com/download
```

4. **Download AI Model**
```bash
# Start Ollama service
ollama serve

# In another terminal, download model
ollama pull mistral:latest    # Main model (4GB)
```

5. **Test Setup**
```bash
python test_ollama.py
```

## 📊 Demo Comparison

| Feature | Web App | Command Line |
|---------|---------|--------------|
| **Interface** | Web Browser | Terminal |
| **AI Model** | Mistral (4GB) | Mistral (4GB) |
| **Agents** | 2 (Research + Write) | 2 (Research + Write) |
| **Topics** | Any topic | Any topic |
| **Output** | Web + Download | File + Terminal |
| **Best For** | Presentations | Development |

## 🔍 Troubleshooting

### Common Issues

**❌ "crewai could not be resolved" (Linter Error)**
- This is normal - your IDE needs the conda environment activated
- Run: `conda activate crewai-free-demo` before running demos

**❌ "Ollama connection refused"**
```bash
# Start Ollama service
ollama serve

# Check if running
ollama ps
```

**❌ "Model not found"**
```bash
# Download required model
ollama pull mistral:latest

# Verify download
ollama list
```

**❌ "Streamlit command not found"**
```bash
# Activate environment first
conda activate crewai-free-demo

# Or install manually
pip install streamlit>=1.28.0
```

**❌ Out of memory errors**
```bash
# Close other applications
# Minimum 4GB RAM required for Mistral model

# Check memory usage
ollama ps
```

### Testing Your Setup

1. **Test Ollama Connection**
```bash
python test_ollama.py
```

2. **Test Web App**
```bash
streamlit run streamlit_app.py
```

## 📁 Project Structure

```
free-crewai-demo/
├── 🚀 DEMOS
│   ├── streamlit_app.py          # Web interface demo
│   └── crewai_free_demo.py       # Command-line demo
├── 🔧 SETUP
│   ├── activate_install_dependencies.sh  # Environment setup
│   ├── setup_ollama.sh           # Ollama installation
│   ├── requirements.txt          # Python dependencies
│   └── environment.yml           # Conda environment
├── 🧪 TESTING
│   └── test_ollama.py            # Connection testing
└── 📚 DOCUMENTATION
    ├── README.md                 # This file
    └── STREAMLIT_README.md       # Detailed web app guide
```

## 🎯 Perfect For

- **🎓 Learning CrewAI** without spending money
- **🔬 Prototyping** AI workflows locally
- **🔒 Privacy-sensitive** projects
- **📱 Offline development** environments  
- **🏫 Educational** purposes and workshops
- **💼 Professional presentations** with web interface

## 💡 Pro Tips

### For Best Performance
- **Keep Ollama running**: Leave `ollama serve` in background
- **First run is slower**: Model loading takes 30-60 seconds initially
- **Monitor resources**: Use `ollama ps` to see active models
- **Close unused apps**: Free up RAM for better performance

### For Development
- **Modify agent roles**: Edit the agent descriptions in demo files
- **Try different models**: Use `ollama list` to see available models
- **Experiment with prompts**: Customize the task descriptions
- **Add more agents**: Extend the crew with additional specialists

## 📈 Next Steps

### Immediate Next Steps
1. **Run both demos** to understand different approaches
2. **Try various research topics** in the web app
3. **Modify agent roles** to suit your needs
4. **Experiment with different models** (`ollama pull <model>`)

### Advanced Exploration
- **Custom Workflows**: Create domain-specific agent teams
- **Model Comparison**: Try different Ollama models
- **Integration**: Connect to your existing Python projects
- **Scaling**: Add more agents for complex workflows

## 🆚 Why This Approach?

| Feature | This Project | OpenAI API | Other Solutions |
|---------|--------------|------------|-----------------|
| **Cost** | $0.00 | ~$0.002/run | Varies |
| **Privacy** | 100% Local | Data sent to API | Varies |
| **Setup** | One-time | API key needed | Complex |
| **Internet** | Not required* | Always required | Usually required |
| **Rate Limits** | None | Yes | Usually yes |
| **Customization** | Full control | Limited | Limited |

*After initial model download

## 🎉 Ready to Start?

Choose your preferred method:

**🚀 Quick Start (Recommended)**
```bash
source activate_install_dependencies.sh
./setup_ollama.sh
streamlit run streamlit_app.py
```

**🔧 Manual Setup**
```bash
conda create -n crewai-free-demo python=3.11 -y
conda activate crewai-free-demo
pip install -r requirements.txt
# ... follow manual setup steps above
```

**⚡ Just Test It**
```bash
conda activate crewai-free-demo
python crewai_free_demo.py
```

---

**🎯 Questions? Issues? Check `STREAMLIT_README.md` for detailed web app instructions!**

*Enjoy your free, private, powerful AI development environment!* 🚀 