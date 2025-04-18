from flask import Blueprint, jsonify, request
from backend.db_connection import db

medications = Blueprint("medications", __name__)

@medications.route("/medications", methods=["GET"])
def get_medications():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Medication;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@medications.route("/medications", methods=["POST"])
def create_medication():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO Medication (name, description) VALUES (%s, %s)",
        (data["name"], data["description"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Medication added"}), 201
