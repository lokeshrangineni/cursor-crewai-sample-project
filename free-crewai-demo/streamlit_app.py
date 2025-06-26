import streamlit as st
import os
import time
from datetime import datetime

# Import our CrewAI demo functions directly
from crewai_free_demo import run_research, check_ollama_setup

# Configure the Streamlit page
st.set_page_config(
    page_title="🚀 AI Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def check_system_status():
    """Check if the system is ready for research."""
    try:
        # Use the same check as the main demo
        import subprocess
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and 'mistral:latest' in result.stdout:
            return True, "✅ Ollama is ready with Mistral model"
        else:
            return False, "❌ Mistral model not found. Please run: ollama pull mistral:latest"
    except subprocess.TimeoutExpired:
        return False, "⏰ Ollama connection timeout"
    except FileNotFoundError:
        return False, "❌ Ollama not installed. Please install from https://ollama.com"
    except Exception as e:
        return False, f"❌ Error: {str(e)}"

def get_research_filename(topic):
    """Generate filename for the research report."""
    return topic.lower().replace(' ', '_').replace('-', '_') + '_research_report.md'

def main():
    # Header
    st.markdown('<h1 class="main-header">🚀 AI Research Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Powered by Free Local AI (Ollama + Mistral) & CrewAI</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 System Status")
        
        # Check system status
        if st.button("🔄 Check System Status"):
            with st.spinner("Checking Ollama..."):
                status, message = check_system_status()
                if status:
                    st.success(message)
                else:
                    st.error(message)
        
        st.markdown("---")
        st.header("📊 Features")
        st.markdown("""
        - 🆓 **100% Free** - No API costs
        - 🔒 **Private** - All data stays local  
        - 🤖 **AI-Powered** - CrewAI + Mistral
        - 📝 **Professional** - Markdown reports
        - ⚡ **Fast** - Local processing
        """)
        
        st.markdown("---")
        st.header("💡 Example Topics")
        example_topics = [
            "Artificial Intelligence",
            "Quantum Computing", 
            "Climate Change",
            "Blockchain Technology",
            "Space Exploration",
            "Renewable Energy",
            "Cybersecurity",
            "Biotechnology"
        ]
        
        for topic in example_topics:
            if st.button(f"📋 {topic}", key=f"example_{topic}"):
                st.session_state.research_topic = topic
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎯 Research Topic")
        
        # Topic input
        topic = st.text_input(
            "Enter the topic you'd like to research:",
            value=st.session_state.get('research_topic', ''),
            placeholder="e.g., Machine Learning, Climate Change, Space Exploration...",
            help="Enter any topic you want to research. The AI will create a comprehensive report."
        )
        
        # Research button
        if st.button("🚀 Start Research", type="primary", disabled=not topic.strip()):
            if topic.strip():
                st.session_state.research_topic = topic.strip()
                st.session_state.research_started = True
                st.rerun()
    
    with col2:
        st.header("📈 Stats")
        st.metric("💰 Cost", "$0.00", "100% Free")
        st.metric("🔒 Privacy", "100%", "Local AI")
        st.metric("⚡ Speed", "~2 min", "Fast processing")
    
    # Research execution
    if st.session_state.get('research_started', False):
        topic = st.session_state.research_topic
        
        st.markdown("---")
        st.header(f"🔬 Researching: {topic}")
        
        # Progress indicators
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Check system first
        status_text.text("🔍 Checking system status...")
        progress_bar.progress(10)
        
        system_ok, system_msg = check_system_status()
        if not system_ok:
            st.error(f"System Error: {system_msg}")
            st.session_state.research_started = False
            return
        
        # Start research
        status_text.text("🤖 Starting AI research agents...")
        progress_bar.progress(25)
        
        # Show progress updates
        status_text.text("📊 Research Agent analyzing topic...")
        progress_bar.progress(50)
        
        status_text.text("✏️ Writing Agent creating report...")
        progress_bar.progress(75)
        
        # Run the actual research using direct function call
        try:
            # This is much cleaner - direct function call!
            success, research_content, blog_post, filename = run_research(topic)
            
            if success:
                progress_bar.progress(100)
                status_text.text("✅ Research completed successfully!")
                
                # Display results
                st.success("🎉 Research completed successfully!")
                
                # Display the generated report
                if filename and os.path.exists(filename):
                    with open(filename, 'r') as f:
                        report_content = f.read()
                    
                    # Display report
                    st.markdown("---")
                    st.header("📋 Generated Research Report")
                    
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**File:** `{filename}`")
                    with col2:
                        # Download button
                        st.download_button(
                            label="📥 Download Report",
                            data=report_content,
                            file_name=filename,
                            mime="text/markdown"
                        )
                    
                    # Show report content
                    with st.expander("📖 View Report Content", expanded=True):
                        st.markdown(report_content)
                    
                    # Show blog post
                    if blog_post:
                        st.markdown("---")
                        st.header("📝 Generated Blog Post")
                        st.markdown(blog_post)
                else:
                    st.warning(f"Report file `{filename}` not found, but research completed.")
                    if research_content:
                        st.markdown("---")
                        st.header("📋 Research Results")
                        st.markdown(research_content)
                    if blog_post:
                        st.markdown("---")
                        st.header("📝 Blog Post")
                        st.markdown(blog_post)
                
            else:
                st.error("❌ Research failed. Please check the system status and try again.")
                
        except Exception as e:
            st.error(f"❌ Error during research: {str(e)}")
            
        # Reset state
        st.session_state.research_started = False

if __name__ == "__main__":
    main() 