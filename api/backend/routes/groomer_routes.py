from flask import Blueprint, jsonify, request
from backend.db_connection import db

groomers = Blueprint("groomers", __name__)

@groomers.route("/groomers", methods=["GET"])
def get_groomers():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM PetGroomer;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@groomers.route("/groomers", methods=["POST"])
def create_groomer():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO PetGroomer (name, email, phone, salon_name) VALUES (%s, %s, %s, %s)",
        (data["name"], data["email"], data["phone"], data["salon_name"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Groomer added"}), 201
