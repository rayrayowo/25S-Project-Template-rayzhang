from flask import Blueprint, jsonify, request
from datetime import datetime

exercise = Blueprint("exercise", __name__)

# 模拟运动数据的“数据库”
exercise_list = []

# Route 1: GET /exercise
@exercise.route("/exercise", methods=["GET"])
def get_exercise():
    return jsonify(exercise_list)

# Route 2: POST /exercise
@exercise.route("/exercise", methods=["POST"])
def create_exercise():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["pet_id", "date", "duration_minutes", "activity_type", "notes"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 exercise_id 和 created_at
    new_id = len(exercise_list) + 1
    data["exercise_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到模拟数据库
    exercise_list.append(data)

    return jsonify({
        "message": "Exercise data added successfully!",
        "exercise": data
    }), 201

