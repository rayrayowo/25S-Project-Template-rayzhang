from flask import Blueprint, jsonify, request
from backend.db_connection import db

grooming_records = Blueprint("grooming-records", __name__)

@grooming_records.route("/grooming-records", methods=["GET"])
def get_grooming_records():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM GroomingRecord;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@grooming_records.route("/grooming-records", methods=["POST"])
def create_grooming_record():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO GroomingRecord (appointment_id, groomer_id, services, notes) VALUES (%s, %s, %s, %s)",
        (data["appointment_id"], data["groomer_id"], data["services"], data["notes"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Grooming-record added"}), 201
