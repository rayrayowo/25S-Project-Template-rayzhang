from flask import Blueprint, jsonify, request
from backend.db_connection import db

checkups = Blueprint("checkups", __name__)

@checkups.route("/checkups", methods=["GET"])
def get_checkups():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Checkup;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@checkups.route("/checkups", methods=["POST"])
def create_checkup():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO Checkup (appointment_id, vet_id, diagnosis) VALUES (%s, %s, %s)",
        (data["appointment_id"], data["vet_id"], data["diagnosis"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Checkup added"}), 201
