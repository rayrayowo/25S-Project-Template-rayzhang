from flask import Blueprint, jsonify, request
from backend.db_connection import db

exercise = Blueprint("exercise", __name__)

@exercise.route("/exercise", methods=["GET"])
def get_exercise():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM ExerciseData;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@exercise.route("/exercise", methods=["POST"])
def create_exercis():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO ExerciseData (pet_id, date, duration_minutes, activity_type, notes) VALUES (%s, %s, %s, %s, %s)",
        (data["pet_id"], data["date"], data["duration_minutes"], data["activity_type"], data["notes"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Exercis added"}), 201
