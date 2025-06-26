#!/usr/bin/env python3
"""
FREE CrewAI Demo - Ollama + Llama 3.2 3B
========================================

The BEST free alternative to paid AI APIs:
✅ 100% Free - No API keys or billing required
✅ Reliable - Runs locally, no internet dependency  
✅ Low Resources - Only 3GB RAM needed
✅ Great Quality - Meta's latest Llama 3.2 model
✅ Privacy - Your data stays on your machine

Perfect for learning CrewAI without any costs!
"""

import os
import sys
from crewai import Agent, Task, Crew
# Using string-based LLM config for CrewAI 0.134.0 - no LangChain import needed

def check_ollama_setup():
    """Check if Ollama is properly set up with the required model."""
    
    print("🔍 Checking Ollama setup...")
    
    try:
        # Test Ollama connection using subprocess (no LangChain needed)
        import subprocess
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if 'mistral:latest' in result.stdout:
            print("✅ Ollama is ready with Mistral!")
            return True
        else:
            return False
            
    except Exception as e:
        print("❌ Ollama setup issue detected")
        print(f"Error: {str(e)}")
        
        print("\n🚀 QUICK FIX GUIDE:")
        print("1. Install Ollama: https://ollama.com/download")
        print("2. Download model: ollama pull llama3.2:3b")
        print("3. Start service: ollama serve")
        print("4. Re-run this demo")
        
        print("\n💡 Need help? Run: ./setup_ollama.sh")
        return False

def run_research(topic):
    """Run the CrewAI research workflow for a given topic.
    
    Args:
        topic (str): The research topic
        
    Returns:
        tuple: (success: bool, research_content: str, blog_post: str, filename: str)
    """
    
    # Check setup first
    if not check_ollama_setup():
        return False, None, None, None
    
    try:
        print("🤖 Model loaded: Mistral (4GB)")
        print(f"🎯 Task: {topic} Research Report + Blog Post")
        print()
        
        # Create research agent
        researcher = Agent(
            role="Research Specialist", 
            goal="Research and analyze any topic with excellent markdown formatting",
            backstory="You are an expert researcher and technical writer who creates well-structured, professionally formatted markdown reports on any topic. You excel at organizing information with clear headings, bullet points, and logical flow.",
            llm="ollama/mistral:latest",
            verbose=False,
            allow_delegation=False
        )
        
        # Create writing agent
        writer = Agent(
            role="Content Writer", 
            goal="Create engaging blog posts based on research",
            backstory="You are a skilled content writer who transforms research into clear, engaging articles.",
            llm="ollama/mistral:latest",
            verbose=False,
            allow_delegation=False
        )
        
        # Define research task
        research_task = Task(
            description=f"""Research the topic '{topic}' and create a well-formatted markdown report with the following structure:

# {topic} Research Report

## 1. Overview
- Provide a clear, comprehensive overview of {topic}
- Include key characteristics and important aspects

## 2. Key Areas/Applications
- List and explain 3 major areas or applications related to {topic}
- Use bullet points and subheadings
- Include real-world examples

## 3. Current Trends/Developments
- Identify and explain 2 important current trends or recent developments
- Discuss implications and potential impact

## 4. Conclusion
- Summarize key findings
- Provide forward-looking insights

Use proper markdown formatting with headers, bullet points, and clear sections.""",
            agent=researcher,
            expected_output=f"A well-formatted markdown research report about {topic} with proper headings, bullet points, and clear structure"
        )
        
        # Define writing task (depends on research)
        writing_task = Task(
            description=f"Based on the research report, write a 100-word blog post about {topic} that is engaging and informative for general readers.",
            agent=writer,
            expected_output=f"A 100-word engaging blog post about {topic}",
            context=[research_task]  # This task depends on research_task output
        )
        
        # Create crew with both agents
        crew = Crew(
            agents=[researcher, writer],
            tasks=[research_task, writing_task],
            verbose=False
        )
        
        print("🚀 Starting FREE AI workflow...")
        print("⏱️  This may take 1-2 minutes with local processing...")
        print()
        
        # Execute the workflow
        print("🔍 Step 1: Research Agent working...")
        print("✏️  Step 2: Writing Agent working...")
        
        # Execute crew and capture results
        result = crew.kickoff()
        
        # Try to get the research task output from crew execution
        research_output = None
        if hasattr(crew, 'tasks') and len(crew.tasks) > 0:
            # Get the first task (research task) output
            research_output = getattr(crew.tasks[0], 'output', None)
            if research_output and hasattr(research_output, 'raw_output'):
                research_content = research_output.raw_output
            elif research_output:
                research_content = str(research_output)
            else:
                research_content = "Research was completed but output not captured"
        else:
            research_content = "Research was completed but output not captured"
        
        # Create filename from topic
        filename = topic.lower().replace(' ', '_').replace('-', '_') + '_research_report.md'
        
        # Save research report to file
        with open(filename, 'w') as f:
            # Add metadata header
            f.write("---\n")
            f.write(f"title: {topic} Research Report\n")
            f.write("generated_by: Research Specialist\n")
            f.write("date: " + str(__import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")
            f.write("model: Ollama + Mistral (Free Local AI)\n")
            f.write("---\n\n")
            
            # Write the research content (should already be well-formatted markdown)
            f.write(research_content)
            
            # Add footer
            f.write("\n\n---\n")
            f.write("*This report was generated using free local AI (Ollama + Mistral)*\n")
        
        print(f"📁 Research report saved to: {filename}")
        
        return True, research_content, str(result), filename
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        
        if "connection" in str(e).lower():
            print("\n💡 Connection issue - try:")
            print("1. ollama serve")
            print("2. Wait 10 seconds, then re-run demo")
            
        elif "model" in str(e).lower():
            print("\n💡 Model issue - try:")
            print("1. ollama pull mistral:latest")
            print("2. ollama list (to verify)")
            
        return False, None, None, None

def main(topic=None):
    """Run the FREE CrewAI demo with local AI.
    
    Args:
        topic (str, optional): Research topic. If None, will prompt user for input.
    """
    
    print("🆓 FREE CrewAI Demo - No API Costs!")
    print("=" * 40)
    print("Using: Ollama + Mistral (Local AI)")
    print()
    
    # Get research topic from user or parameter
    if topic is None:
        print("📝 What topic would you like to research?")
        print("Examples: 'Machine Learning', 'Climate Change', 'Blockchain Technology', 'Space Exploration'")
        topic = input("Enter your research topic: ").strip()
        
        if not topic:
            print("❌ No topic provided. Exiting...")
            return False
    
    print(f"🎯 Research Topic: {topic}")
    print()
    
    # Run the research
    success, research_content, blog_post, filename = run_research(topic)
    
    if success:
        print("\n" + "="*50)
        print("✅ FREE CrewAI Demo Completed!")
        print("="*50)
        print("📋 RESEARCH REPORT:")
        print("-" * 40)
        print("✅ Research was completed by the Research Specialist")
        print(f"📊 The research covered: {topic} overview, applications, and current trends")
        print(f"📁 Full research report saved to: {filename}")
        print("-" * 40)
        print("\n📄 FINAL BLOG POST:")
        print("-" * 30)
        print(blog_post)
        print("-" * 30)
        
        print("\n💡 Demo Stats:")
        print(f"💰 Cost: $0.00 (100% FREE!)")
        print(f"🤖 Model: Mistral (Local)")
        print(f"🔒 Privacy: All data stayed on your machine")
        print(f"🌐 Internet: Not required after setup")
        
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        import traceback
        print(f"Full traceback:\n{traceback.format_exc()}") 