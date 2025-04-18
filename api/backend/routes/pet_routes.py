from flask import Blueprint, jsonify, request
from datetime import datetime

pets = Blueprint("pets", __name__)

# 模拟宠物数据的“数据库”
pets_list = []

# Route 1: GET /pets
@pets.route("/pets", methods=["GET"])
def get_pets():
    return jsonify(pets_list)

# Route 2: POST /pets
@pets.route("/pets", methods=["POST"])
def create_pet():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["owner_id", "name", "species", "breed", "age", "gender"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 pet_id 和 created_at
    new_id = len(pets_list) + 1
    data["pet_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    pets_list.append(data)

    return jsonify({
        "message": "Pet added successfully!",
        "pet": data
    }), 201

