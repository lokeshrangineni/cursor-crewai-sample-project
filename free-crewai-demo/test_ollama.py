#!/usr/bin/env python3
"""
Simple Ollama Test Script
========================
Debug the connection between Python and Ollama
"""

import traceback

def test_ollama_direct():
    """Test direct Ollama connection."""
    print("🔍 Testing direct Ollama connection...")
    
    try:
        from langchain_ollama import OllamaLLM
        
        # Create LLM instance
        llm = OllamaLLM(
            model="llama3.2:3b",
            temperature=0.3,
            base_url="http://localhost:11434"  # Explicit base URL
        )
        
        print("✅ LLM instance created successfully")
        
        # Test simple invoke
        print("🧪 Testing simple invoke...")
        response = llm.invoke("Say 'Hello World' and nothing else.")
        print(f"✅ Response: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("🔍 Full traceback:")
        traceback.print_exc()
        return False

def test_ollama_python_client():
    """Test with Python ollama client directly."""
    print("\n🔍 Testing Python ollama client...")
    
    try:
        import ollama
        
        response = ollama.chat(model='llama3.2:3b', messages=[
            {
                'role': 'user',
                'content': 'Say "Hello World" and nothing else.',
            },
        ])
        
        print(f"✅ Direct client response: {response['message']['content']}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("🔍 Full traceback:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🆓 Ollama Connection Test")
    print("=" * 30)
    
    # Test 1: Direct Ollama
    success1 = test_ollama_direct()
    
    # Test 2: Python client
    success2 = test_ollama_python_client()
    
    print("\n📊 Test Results:")
    print(f"LangChain Ollama: {'✅ PASS' if success1 else '❌ FAIL'}")
    print(f"Python Client: {'✅ PASS' if success2 else '❌ FAIL'}")
    
    if success1 and success2:
        print("\n🎉 All tests passed! Ollama is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.") 