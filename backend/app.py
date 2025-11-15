from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pathlib import Path

# Charge le fichier .env avec le chemin explicite
env_path = Path(__file__).parent / '.env'
print(f"DEBUG: Chargement du .env depuis: {env_path}")
print(f"DEBUG: Le fichier existe: {env_path.exists()}")
load_dotenv(str(env_path), override=True)

# Vérifie que le token est chargé
token = os.getenv('HUGGINGFACE_TOKEN')
print(f"DEBUG: Token chargé: {token[:20] if token else 'None'}...")

# Importe les modules AI
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
    print("DEBUG: /health route called")
    return jsonify({
        "status": "healthy",
        "service": "EchoPet Backend",
        "timestamp": "2025-11-15 16:00:00"
    })

@app.route('/course/')
def generate_course():
    print("DEBUG: /course/ route called with args:", dict(request.args))
    language = request.args.get('lang', 'python').lower()
    level = request.args.get('level', 'beginner').lower()
    
    try:
        # Vérifie le token HuggingFace
        has_token = HFConfig.validate_token()
        print(f"DEBUG: HF Token valide: {has_token}")
        
        # Utilise l'IA pour générer le cours
        course_gen = CourseGenerator()
        course_content = course_gen.generate_course(language, level)
        
        print(f"DEBUG: Cours généré avec succès pour {language} ({level})")
        
        return jsonify({
            "success": True,
            "ai_generated": has_token,
            "data": course_content
        })
    except Exception as e:
        print(f"❌ ERREUR dans /course/: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Erreur lors de la génération du cours"
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
            "explanation": f"{language.title()} is a general-purpose programming language used for various applications."
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
    print("🚀 EchoPet Backend started on http://127.0.0.1:5000")
    print("📚 Available endpoints:")
    print("   GET /")
    print("   GET /health") 
    print("   GET /course/?lang=python&level=beginner")
    print("   GET /quiz/?lang=html&level=intermediate&questions=5")
    app.run(debug=True, host='0.0.0.0', port=5000)