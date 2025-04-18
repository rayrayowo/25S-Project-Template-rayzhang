from flask import Blueprint, jsonify, request
from datetime import datetime

owners = Blueprint("owners", __name__)

# 模拟宠物主人数据库
owners_list = []

# Route 1: GET /owners
@owners.route("/owners", methods=["GET"])
def get_owners():
    return jsonify(owners_list)

# Route 2: POST /owners
@owners.route("/owners", methods=["POST"])
def create_owner():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["name", "email", "phone", "address"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 owner_id 和 created_at
    new_id = len(owners_list) + 1
    data["owner_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    owners_list.append(data)

    return jsonify({
        "message": "Owner added successfully!",
        "owner": data
    }), 201

