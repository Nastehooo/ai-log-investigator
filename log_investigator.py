import os
from anthropic import Anthropic
from rich.console import Console

# Initialize Anthropic client with API key from environment
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
console = Console()

def load_logs(file_path="logs.txt"):
    """Read logs from a text file"""
    with open(file_path, "r") as f:
        return f.read()

def analyze_logs(logs):
    """Send logs to Claude for analysis"""
    prompt = f"""
    You are a Site Reliability Engineer.
    Analyze the following logs and suggest:
    1. The most likely root cause
    2. Recommended next steps

    Logs:
    {logs}
    """
    response = client.messages.create(
        model="claude-sonnet-4-20250514",  # ✅ latest stable Claude Sonnet model
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

if __name__ == "__main__":
    try:
        logs = load_logs()
        console.print("[bold green]Analyzing logs with Claude...[/bold green]")
        result = analyze_logs(logs)
        console.print("\n[bold cyan]AI Analysis Result:[/bold cyan]")
        console.print(result)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

