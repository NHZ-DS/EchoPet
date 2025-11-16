from flask import Blueprint, request, jsonify

quiz_check_bp = Blueprint('quiz_check', __name__)

# Exemple de stockage temporaire des bonnes réponses
# Dans la vraie logique, tu pourrais les stocker en mémoire ou en DB
quiz_answers_db = {}  # {quiz_id: {question_id: correct_answer}}

@quiz_check_bp.route('/check', methods=['POST'])
def check_answer():
    data = request.json
    quiz_id = data.get("quiz_id")       # identifiant du quiz
    question_id = data.get("question_id")
    user_answer = data.get("answer")    # index choisi (0–3)

    # Vérifier si on a les réponses pour ce quiz
    if quiz_id not in quiz_answers_db:
        return jsonify({"error": "Quiz not found"}), 404

    correct_answer = quiz_answers_db[quiz_id].get(question_id)

    if correct_answer is None:
        return jsonify({"error": "Question not found"}), 404

    # Vérification
    is_correct = (user_answer == correct_answer)

    # Attribution XP/coins
    coins = 10 if is_correct else 0
    xp = 5 if is_correct else 0

    return jsonify({
        "question_id": question_id,
        "correct": is_correct,
        "coins_awarded": coins,
        "xp_awarded": xp,
        "message": "Well done!" if is_correct else "Try again!"
    })
