from flask import Blueprint, jsonify, request
from backend.db_connection import db

events = Blueprint("events", __name__)

@events.route("/events", methods=["GET"])
def get_events():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM PetEvent;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@events.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO PetEvent (pet_id, event_type, description, event_date) VALUES (%s, %s, %s, %s)",
        (data["pet_id"], data["event_type"], data["description"], data["event_date"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Event added"}), 201
