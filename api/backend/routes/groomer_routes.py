from flask import Blueprint, jsonify, request
from datetime import datetime

groomers = Blueprint("groomers", __name__)

# 模拟宠物美容师数据的“数据库”
groomers_list = []

# Route 1: GET /groomers
@groomers.route("/groomers", methods=["GET"])
def get_groomers():
    return jsonify(groomers_list)

# Route 2: POST /groomers
@groomers.route("/groomers", methods=["POST"])
def create_groomer():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["name", "email", "phone", "salon_name"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 groomer_id 和 created_at
    new_id = len(groomers_list) + 1
    data["groomer_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    groomers_list.append(data)

    return jsonify({
        "message": "Groomer added successfully!",
        "groomer": data
    }), 201
