from flask import Blueprint, jsonify, request
from datetime import datetime

medications = Blueprint("medications", __name__)


medications_list = []


@medications.route("/medications", methods=["GET"])
def get_medications():
    return jsonify(medications_list)


@medications.route("/medications", methods=["POST"])
def create_medication():
    data = request.get_json()


    required_fields = ["name", "description"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400


    new_id = len(medications_list) + 1
    data["medication_id"] = new_id
    data["created_at"] = datetime.now().isoformat()


    medications_list.append(data)

    return jsonify({
        "message": "Medication added successfully!",
        "medication": data
    }), 201

