from flask import Blueprint, jsonify, request

appointments = Blueprint("appointments", __name__)

appointments_list = [
    {"id": 1, "pet": "Buddy", "date": "2025-04-10", "service": "Grooming"},
    {"id": 2, "pet": "Milo", "date": "2025-04-20", "service": "Vet Checkup"}
]
# Route 1: GET /appointments
@appointments.route("/appointments", methods=["GET"])
def get_appointments():
    return jsonify(appointments_list)

# Route 2: POST /appointments
@appointments.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()

    # 自动生成新的 ID
    new_id = max(a["id"] for a in appointments_list) + 1 if appointments_list else 1
    data["id"] = new_id

    appointments_list.append(data)

    return jsonify({
        "message": "Appointment created successfully!",
        "appointment": data,
        "total_appointments": len(appointments_list)
    }), 201