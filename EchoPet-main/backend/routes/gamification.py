from flask import Blueprint, jsonify
import random

gamification_bp = Blueprint('gamification', __name__)

@gamification_bp.route('/challenge', methods=['GET'])
def challenge():
    challenges = [
        "Solve a riddle: What has keys but can't open locks?",
        "Fix the pet's mistake: pritn('Hello')"
    ]
    return jsonify({"challenge": random.choice(challenges)})

@gamification_bp.route('/debate', methods=['GET'])
def classroom_debate():
    debates = [
        "Cat says recursion is best, Fox says iteration is better. Who is right?",
        "Fox wants to use while loop, Cat prefers for loop. Guide them!"
    ]
    return jsonify({"debate": random.choice(debates)})
