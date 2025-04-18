from flask import Blueprint, jsonify, request
from datetime import datetime

community = Blueprint("community", __name__)

# 模拟社区帖子数据的“数据库”
community_list = []

# Route 1: GET /community
@community.route("/community", methods=["GET"])
def get_community():
    return jsonify(community_list)

# Route 2: POST /community
@community.route("/community", methods=["POST"])
def create_community():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["pet_id", "content", "post_date", "likes"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 community_id 和 created_at
    new_id = len(community_list) + 1
    data["community_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    community_list.append(data)

    return jsonify({
        "message": "Community post added successfully!",
        "community": data
    }), 201
