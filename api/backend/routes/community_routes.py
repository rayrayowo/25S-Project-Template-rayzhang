from flask import Blueprint, jsonify, request
from backend.db_connection import db

community = Blueprint("community", __name__)

@community.route("/community", methods=["GET"])
def get_community():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Community;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@community.route("/community", methods=["POST"])
def create_communit():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO Community (pet_id, content, post_date, likes) VALUES (%s, %s, %s, %s)",
        (data["pet_id"], data["content"], data["post_date"], data["likes"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Communit added"}), 201
