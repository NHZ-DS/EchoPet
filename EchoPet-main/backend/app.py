from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pathlib import Path
import requests

# Load .env file with explicit path
env_path = Path(__file__).parent / '.env'
load_dotenv(str(env_path), override=True)

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi4")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

app = Flask(__name__)
CORS(app)



def ask_ollama(prompt: str, model: str = OLLAMA_MODEL):
    """Send prompt to local Ollama model and return merged text response."""
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True,
            timeout=120
        )

        if response.status_code != 200:
            print("Ollama returned:", response.text)
            return None

        full_text = ""


        for line in response.iter_lines():
            if not line:
                continue

            chunk = line.decode("utf-8")


            if chunk.startswith("{"):
                try:
                    import json
                    obj = json.loads(chunk)
                    full_text += obj.get("response", "")
                    continue
                except:
                    pass


            full_text += chunk

        return full_text.strip()

    except Exception as e:
        print(f"❌ Ollama request failed: {e}")
        return None


@app.route('/')
def home():
    return {
        "message": "EchoPet Backend API - Running (Local Ollama Mode)!",
        "version": "2.0",
        "status": "active",
        "ollama_model": OLLAMA_MODEL,
        "endpoints": {
            "course": "/course/?lang=python&level=beginner",
            "quiz": "/quiz/?lang=html&level=intermediate&questions=5",
            "health": "/health"
        }
    }

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "EchoPet Backend",
        "ollama_model": OLLAMA_MODEL
    })

@app.route('/course/')
def generate_course():
    language = request.args.get('lang', 'python').lower()
    level = request.args.get('level', 'beginner').lower()

    prompt = f"""
    Generate a structured short programming course.
    Language: {language}
    Level: {level}.
    Include:
    - 2 lessons
    - Simple explanations only
    - Example code
    - Mini tasks for practice
    Format response as JSON with keys: title, lessons[].
    very compact
    """

    course_content = ask_ollama(prompt)

    if not course_content:
        return jsonify({"success": False, "error": "Ollama generation failed"}), 500

    return jsonify({
        "success": True,
        "ai_generated": True,
        "language": language,
        "level": level,
        "data": course_content
    })

@app.route('/quiz/')
def generate_quiz():
    language = request.args.get('lang', 'python').lower()
    level = request.args.get('level', 'beginner').lower()
    num_questions = request.args.get('questions', 5, type=int)

    questions = []
    for i in range(num_questions):
        questions.append({
            "id": i + 1,
            "question": f"What is the main purpose of {language} programming?",
            "options": [
                "Web development only",
                "Mobile applications only",
                f"General purpose {language} programming",
                "Data analysis exclusively"
            ],
            "correct_answer": 2,
            "explanation": f"{language.title()} is a general-purpose programming language."
        })

    quiz_content = {
        "title": f"{language.title()} {level.title()} Level Quiz",
        "language": language,
        "level": level,
        "questions": questions
    }

    return jsonify({
        "success": True,
        "data": quiz_content
    })

if __name__ == '__main__':
    print(f"🚀 EchoPet Backend starting with Ollama model: {OLLAMA_MODEL}")
    app.run(debug=True, host='127.0.0.1', port=5000)
