from flask import Blueprint, jsonify, request
from datetime import datetime

analytics = Blueprint("analytics", __name__)

# 用于模拟数据库的内存列表
analytics_list = []

# Route 1: GET /analytics
@analytics.route("/analytics", methods=["GET"])
def get_analytics():
    return jsonify(analytics_list)

# Route 2: POST /analytics
@analytics.route("/analytics", methods=["POST"])
def create_analytic():
    data = request.get_json()

    # 检查是否缺字段
    required_fields = ["profile_id", "average_weight", "weight_trend", "recommended_diet"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 自动生成 id 和 created_at 时间戳
    data["analytic_id"] = len(analytics_list) + 1
    data["created_at"] = datetime.now().isoformat()

    # 加入模拟数据库
    analytics_list.append(data)

    return jsonify({
        "message": "Analytic added successfully!",
        "analytic": data
    }), 201
