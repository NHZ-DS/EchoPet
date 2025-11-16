from flask import Blueprint, request, jsonify

pet_reaction_bp = Blueprint('pet_reaction', __name__)

@pet_reaction_bp.route('/reaction', methods=['GET'])
def pet_reaction():
    # Le frontend envoie ?result=correct / wrong / idle
    result = request.args.get("result", "idle")

    reactions = {
        "correct": {"reaction": "happy", "message": "Great job! 🎉"},
        "wrong": {"reaction": "sad", "message": "Oops, try again! 😿"},
        "idle": {"reaction": "idle", "message": "I'm waiting... 💤"}
    }

    return jsonify(reactions.get(result, reactions["idle"]))
