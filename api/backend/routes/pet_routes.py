from flask import Blueprint, jsonify, request
from backend.db_connection import db

pets = Blueprint("pets", __name__)

@pets.route("/pets", methods=["GET"])
def get_pets():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Pet;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@pets.route("/pets", methods=["POST"])
def create_pet():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO Pet (owner_id, name, species, breed, age, gender) VALUES (%s, %s, %s, %s, %s, %s)",
        (data["owner_id"], data["name"], data["species"], data["breed"], data["age"], data["gender"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Pet added"}), 201
