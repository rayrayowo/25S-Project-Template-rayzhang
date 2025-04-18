from flask import Blueprint, jsonify, request
from backend.db_connection import db

health_records = Blueprint("health-records", __name__)

@health_records.route("/health-records", methods=["GET"])
def get_health_records():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM HealthRecord;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@health_records.route("/health-records", methods=["POST"])
def create_health_record():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO HealthRecord (profile_id, date, weight, diet, notes) VALUES (%s, %s, %s, %s, %s)",
        (data["profile_id"], data["date"], data["weight"], data["diet"], data["notes"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Health-record added"}), 201
