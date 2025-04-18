from flask import Blueprint, jsonify, request
from backend.db_connection import db

owners = Blueprint("owners", __name__)

@owners.route("/owners", methods=["GET"])
def get_owners():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM PetOwner;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@owners.route("/owners", methods=["POST"])
def create_owner():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO PetOwner (name, email, phone, address) VALUES (%s, %s, %s, %s)",
        (data["name"], data["email"], data["phone"], data["address"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Owner added"}), 201
