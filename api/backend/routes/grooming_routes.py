from flask import Blueprint, jsonify, request
from datetime import datetime

grooming_records = Blueprint("grooming-records", __name__)

# 用列表模拟数据库
grooming_records_list = []

# GET /grooming-records
@grooming_records.route("/grooming-records", methods=["GET"])
def get_grooming_records():
    return jsonify(grooming_records_list)

# POST /grooming-records
@grooming_records.route("/grooming-records", methods=["POST"])
def create_grooming_record():
    data = request.get_json()

    # 检查必填字段
    required_fields = ["appointment_id", "groomer_id", "services", "notes"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 自动生成 id 和时间
    new_id = len(grooming_records_list) + 1
    data["record_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    grooming_records_list.append(data)

    return jsonify({
        "message": "Grooming record added successfully!",
        "record": data
    }), 201
