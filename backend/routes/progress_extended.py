from flask import Blueprint, request, jsonify
import datetime

progress_extended_bp = Blueprint('progress_extended', __name__)

user_progress = {
    "lessons_completed": 0,
    "coins": 0,
    "xp": 0,
    "streak": 0,
    "last_activity": None
}

@progress_extended_bp.route('/update', methods=['POST'])
def update_progress():
    data = request.json

    user_progress["lessons_completed"] += 1

    user_progress["coins"] += data.get("coins", 10)
    user_progress["xp"] += data.get("xp", 5)

    today = datetime.date.today()
    if user_progress["last_activity"] is None:
        user_progress["streak"] = 1
    else:
        last_day = user_progress["last_activity"]
        if today == last_day:
            pass
        elif today == last_day + datetime.timedelta(days=1):
            user_progress["streak"] += 1
        else:
            
            user_progress["streak"] = 1

    user_progress["last_activity"] = today

    return jsonify(user_progress)

@progress_extended_bp.route('/status', methods=['GET'])
def progress_status():
    return jsonify(user_progress)
