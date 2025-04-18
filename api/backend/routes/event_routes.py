from flask import Blueprint, jsonify, request
from datetime import datetime

events = Blueprint("events", __name__)

# 类似数据库的内存列表
events_list = []

# GET /events — 获取所有事件
@events.route("/events", methods=["GET"])
def get_events():
    return jsonify(events_list)

# POST /events — 创建一个新事件
@events.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # 检查必要字段
    required_fields = ["pet_id", "event_type", "description", "event_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 构建事件数据结构
    new_event = {
        "event_id": len(events_list) + 1,
        "pet_id": data["pet_id"],
        "event_type": data["event_type"],
        "description": data["description"],
        "event_date": data["event_date"],
        "created_at": datetime.now().isoformat()
    }

    events_list.append(new_event)

    return jsonify({
        "message": "Event added successfully!",
        "event": new_event
    }), 201

