from flask import Blueprint, request, jsonify

pet_bp = Blueprint('pet', __name__)

pets = {
    "cat": {"name": "Cat", "personality": "Chill and playful", "level": 1},
    "fox": {"name": "Fox", "personality": "Curious and fast learner", "level": 1}
}

@pet_bp.route('/choose', methods=['POST'])
def choose_pet():
    data = request.json
    pet_choice = data.get("pet", "cat")
    return jsonify({"message": f"You chose {pet_choice}", "pet": pets[pet_choice]})

@pet_bp.route('/status', methods=['GET'])
def pet_status():
    return jsonify({"pets": pets})
