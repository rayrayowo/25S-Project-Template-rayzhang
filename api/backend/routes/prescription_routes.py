from flask import Blueprint, jsonify, request
from backend.db_connection import db

prescriptions = Blueprint("prescriptions", __name__)

@prescriptions.route("/prescriptions", methods=["GET"])
def get_prescriptions():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Prescription;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@prescriptions.route("/prescriptions", methods=["POST"])
def create_prescription():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO Prescription (checkup_id, medication_id, dosage, instructions) VALUES (%s, %s, %s, %s)",
        (data["checkup_id"], data["medication_id"], data["dosage"], data["instructions"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Prescription added"}), 201
