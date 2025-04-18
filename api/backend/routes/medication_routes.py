from flask import Blueprint, jsonify, request
from datetime import datetime

medications = Blueprint("medications", __name__)

# 模拟药物记录数据库
medications_list = []

# Route 1: GET /medications
@medications.route("/medications", methods=["GET"])
def get_medications():
    return jsonify(medications_list)

# Route 2: POST /medications
@medications.route("/medications", methods=["POST"])
def create_medication():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["name", "description"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 medication_id 和 created_at
    new_id = len(medications_list) + 1
    data["medication_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    medications_list.append(data)

    return jsonify({
        "message": "Medication added successfully!",
        "medication": data
    }), 201

