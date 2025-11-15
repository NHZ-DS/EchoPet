from flask import Blueprint, request, jsonify

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/', methods=['GET'])
def get_quiz():
    lang = request.args.get('lang', 'python')
    quiz = {
        "lang": lang,
        "questions": [
            {"q": "What is 2+2?", "options": [2, 3, 4, 5], "answer": 4},
            {"q": "Print in Python?", "options": ["echo()", "print()", "log()", "say()"], "answer": "print()"}
        ]
    }
    return jsonify(quiz)
