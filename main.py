import os
import json
import re
from fastapi import FastAPI, UploadFile, Form, Request, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from anthropic import Anthropic

# Initialize
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def clean_json_response(text):
    cleaned = re.sub(r"^```json|```$", "", text.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r"^```|```$", "", cleaned.strip(), flags=re.MULTILINE)
    return cleaned.strip()

def analyze_logs(logs):
    prompt = f"""
    You are a Site Reliability Engineer.
    Analyze the following logs (from multiple sources) and return ONLY valid JSON with this structure:

    {{
      "root_cause": "string",
      "immediate_actions": ["list", "of", "steps"],
      "investigation": ["list", "of", "steps"],
      "prevention": ["list", "of", "steps"]
    }}

    No explanations. No markdown. Only JSON.

    Logs:
    {logs}
    """
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    raw_output = response.content[0].text
    cleaned_output = clean_json_response(raw_output)
    try:
        return json.loads(cleaned_output)
    except json.JSONDecodeError:
        return {"error": "Claude did not return valid JSON", "raw_output": raw_output}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, log_files: list[UploadFile] = File(...)):
    logs = []
    for file in log_files:
        content = await file.read()
        logs.append(f"\n--- {file.filename} ---\n" + content.decode())
    merged_logs = "\n".join(logs)
    result = analyze_logs(merged_logs)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

