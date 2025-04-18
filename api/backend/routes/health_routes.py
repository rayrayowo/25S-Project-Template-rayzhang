from flask import Blueprint, request, jsonify
from datetime import datetime

health_records = Blueprint("health-records", __name__)

# 模拟健康记录数据库
health_records_list = []

# Route 1: GET /health-records
@health_records.route("/health-records", methods=["GET"])
def get_health_records():
    return jsonify(health_records_list)

# Route 2: POST /health-records
@health_records.route("/health-records", methods=["POST"])
def create_health_record():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["profile_id", "date", "weight", "diet", "notes"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 health_record_id 和 created_at
    new_id = len(health_records_list) + 1
    data["health_record_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    health_records_list.append(data)

    return jsonify({
        "message": "Health-record added successfully!",
        "health_record": data
    }), 201
