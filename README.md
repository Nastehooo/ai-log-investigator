# AI Log Investigator 
An AI-powered web application built with FastAPI that analyzes log files and provides structured insights into root causes, immediate actions, investigation steps, and prevention measures.

# Features
  - Upload a single log file (.log, .txt)
  - AI-powered log analysis using Claude API
  - Categorized results:
    - 🔍 Root Cause
    - ⚡ Immediate Actions
    - 🧪 Investigation Steps
    - 🛡 Prevention Measures
   - Clean, collapsible UI for results

# Installation 
1. Clone the repository:
   > - git clone https://github.com/Nastehooo/ai-log-investigator.git
   > - cd ai-log-investigator

2. Create and activate a virtual environment:
   > python -m venv venv
   > source venv/bin/activate   # macOS/Linux
   > venv\Scripts\activate      # Windows

3. Install dependencies:
   > pip install -r requirements.txt

4. Set up your Anthropic API Key:
    > - export ANTHROPIC_API_KEY="your_api_key_here"   # macOS/Linux
    > - setx ANTHROPIC_API_KEY "your_api_key_here"     # Windows PowerShell
    
# How to Test the Project
1. Start the server:
   > uvicorn main:app --reload
2. Open your browser at:
   > http://127.0.0.1:8000
3. Click Choose Log and upload a single .log file
4. Hit Analyze Logs
5. The AI will return results in sections:
    - ✅ Root Cause
    - ✅ Immediate Actions
    - ✅ Investigation Steps
    - ✅ Prevention Measures
  
# Video Setup
https://github.com/user-attachments/assets/f1be5521-6cfc-468b-ac19-e5bf8bdb253c
  
# Project Structure 
```text
ai-log-investigator/
├── main.py              # FastAPI backend
├── templates/
│   └── index.html       # Frontend UI
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignore venv/logs
