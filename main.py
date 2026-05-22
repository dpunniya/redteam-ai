from fastapi import FastAPI

app = FastAPI(
    title="Red Team AI",
    description="Automated security testing toolkit for LLM applications",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "name": "Red Team AI",
        "description": "LLM Security Testing Toolkit",
        "version": "1.0"
    }

@app.post("/scan")
def scan_prompt(prompt: str):
    
    injection_patterns = [
        "ignore previous instructions",
        "ignore all instructions",
        "you are now",
        "forget everything",
        "disregard your",
        "bypass your",
        "jailbreak",
        "do anything now",
        "DAN",
        "pretend you are",
        "act as if",
        "override",
    ]
    
    prompt_lower = prompt.lower()
    detected = []
    
    for pattern in injection_patterns:
        if pattern.lower() in prompt_lower:
            detected.append(pattern)
    
    if detected:
        return {
            "status": "THREAT DETECTED",
            "risk_level": "HIGH",
            "detected_patterns": detected,
            "prompt": prompt
        }
    else:
        return {
            "status": "CLEAN",
            "risk_level": "LOW",
            "detected_patterns": [],
            "prompt": prompt
        }