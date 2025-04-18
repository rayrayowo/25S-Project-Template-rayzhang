from flask import Blueprint, jsonify, request
from backend.db_connection import db

vets = Blueprint("vets", __name__)

@vets.route("/vets", methods=["GET"])
def get_vets():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Veterinarian;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@vets.route("/vets", methods=["POST"])
def create_vet():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO Veterinarian (name, gender, email, phone, graduate_school, working_hours, clinic_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (data["name"], data["gender"], data["email"], data["phone"], data["graduate_school"], data["working_hours"], data["clinic_id"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Vet added"}), 201
