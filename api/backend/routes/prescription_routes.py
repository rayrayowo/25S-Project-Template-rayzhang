from flask import Blueprint, jsonify, request
from datetime import datetime

prescriptions = Blueprint("prescriptions", __name__)

# 模拟药方数据的“数据库”
prescriptions_list = []

# Route 1: GET /prescriptions
@prescriptions.route("/prescriptions", methods=["GET"])
def get_prescriptions():
    return jsonify(prescriptions_list)

# Route 2: POST /prescriptions
@prescriptions.route("/prescriptions", methods=["POST"])
def create_prescription():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["checkup_id", "medication_id", "dosage", "instructions"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 prescription_id 和 created_at
    new_id = len(prescriptions_list) + 1
    data["prescription_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    prescriptions_list.append(data)

    return jsonify({
        "message": "Prescription added successfully!",
        "prescription": data
    }), 201

