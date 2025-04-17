"""
This module defines the Flask routes for appointments.
NOTE: The data used in these routes is currently hardcoded for demonstration and testing purposes.
In future iterations, this will be replaced with database-backed logic.
"""

# Route 1: GET /appointments
@appointments.route("/appointments", methods=["GET"])
def get_appointments():
    """
    Return a hardcoded list of sample appointments.
    Will be replaced with real database queries in future.
    """
    appointments_list = [
        {"id": 1, "pet": "Buddy", "date": "2025-04-10", "service": "Grooming"},
        {"id": 2, "pet": "Milo", "date": "2025-04-20", "service": "Vet Checkup"}
    ]
    return jsonify(appointments_list)

# Route 2: POST /appointments
@appointments.route("/appointments", methods=["POST"])
def create_appointment():
    """
    Accept a JSON object and return it as confirmation.
    Does not actually store the appointment — this will be implemented later.
    """
    data = request.get_json()
    return jsonify({
        "message": "Appointment created successfully!",
        "appointment": data
    }), 201