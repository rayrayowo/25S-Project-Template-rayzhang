from flask import Blueprint, request, jsonify
from datetime import datetime

checkups = Blueprint("checkups", __name__)

# 用列表模拟数据库
checkups_list = []

# GET /checkups - 获取所有检查记录
@checkups.route("/checkups", methods=["GET"])
def get_checkups():
    return jsonify(checkups_list)

# POST /checkups - 新建一条检查记录
@checkups.route("/checkups", methods=["POST"])
def create_checkup():
    data = request.get_json()

    # 检查必要字段
    required_fields = ["appointment_id", "vet_id", "diagnosis"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 自动生成 ID 和时间戳
    new_id = len(checkups_list) + 1
    data["checkup_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 加入模拟数据库
    checkups_list.append(data)

    return jsonify({
        "message": "Checkup created successfully!",
        "checkup": data
    }), 201
    
