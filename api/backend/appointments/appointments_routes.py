from flask import Blueprint, request, jsonify
from datetime import datetime

appointments = Blueprint("appointments", __name__)

appointments_list = []
# Route 1: GET /appointments
@appointments.route("/appointments", methods=["GET"])
def get_appointments():
    return jsonify(appointments_list)

# Route 2: POST /appointments
@appointments.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()

    # 确保必要字段存在
    required_fields = ["pet_id", "appointment_date", "appointment_time", "appointment_type", "status"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # 生成 appointment_id 和 created_at
    new_id = len(appointments_list) + 1
    data["appointment_id"] = new_id
    data["created_at"] = datetime.now().isoformat()

    # 添加到“数据库”
    appointments_list.append(data)

    return jsonify({
        "message": "Appointment created successfully!",
        "appointment": data
    }), 201