from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file with explicit path
env_path = Path(__file__).parent / '.env'
print(f"DEBUG: Loading .env from: {env_path}")
print(f"DEBUG: File exists: {env_path.exists()}")

load_dotenv(str(env_path), override=True)

# Check if token is loaded (SECURE - don't print actual token)
token = os.getenv('HUGGINGFACE_TOKEN')
print(f"DEBUG: Token loaded: {token is not None}")
print(f"DEBUG: Token valid format: {token and token.startswith('hf_')}")
if token:
    print(f"DEBUG: Token length: {len(token)}")
else:
    print("❌ DEBUG: No token found!")

from ai.hf_config import HFConfig
from ai.course_gen import CourseGenerator

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {
        "message": "EchoPet Backend API - Running!",
        "version": "1.0", 
        "status": "active",
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
        "service": "EchoPet Backend"
    })

@app.route('/course/')
def generate_course():
    language = request.args.get('lang', 'python').lower()
    level = request.args.get('level', 'beginner').lower()
    
    try:
        has_token = HFConfig.validate_token()
        print(f"DEBUG: HF Token valid: {has_token}")
        
        course_gen = CourseGenerator()
        course_content = course_gen.generate_course(language, level)
        
        return jsonify({
            "success": True,
            "ai_generated": has_token,
            "language": language,
            "level": level,
            "data": course_content
        })
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Error generating course"
        }), 500

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
    print("🚀 EchoPet Backend starting...")
    app.run(debug=True, host='127.0.0.1', port=5000)