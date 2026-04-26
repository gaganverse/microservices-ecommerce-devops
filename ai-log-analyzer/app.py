from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_logs(logs):
    prompt = f"""
You are an SRE expert.

Analyze the following logs and provide:
1. Root cause
2. Affected service
3. Suggested fix

Logs:
{logs}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    logs = data.get("logs", "")

    if not logs:
        return jsonify({"error": "No logs provided"}), 400

    result = analyze_logs(logs)

    return jsonify({
        "analysis": result
    })


@app.route("/")
def home():
    return "AI Log Analyzer is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
