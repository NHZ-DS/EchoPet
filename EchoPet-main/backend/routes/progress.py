from flask import Blueprint, request, jsonify

progress_bp = Blueprint('progress', __name__)

user_progress = {"lessons_completed": 0, "coins": 0}

@progress_bp.route('/update', methods=['POST'])
def update_progress():
    data = request.json
    user_progress["lessons_completed"] += 1
    user_progress["coins"] += data.get("coins", 10)
    return jsonify(user_progress)

@progress_bp.route('/status', methods=['GET'])
def progress_status():
    return jsonify(user_progress)
