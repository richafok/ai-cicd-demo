import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def generate_code(requirement):
    payload = {
        "contents": [{
            "parts": [{
                "text": f"""
You are a senior Python engineer.
Generate FastAPI code and pytest tests.

Requirement:
{requirement}

Return only code blocks.
"""
            }]
        }]
    }

    response = requests.post(
        f"{URL}?key={API_KEY}",
        json=payload
    )

    return response.json()

if __name__ == "__main__":
    requirement = "Add a /health endpoint returning status ok"
    print(generate_code(requirement))
