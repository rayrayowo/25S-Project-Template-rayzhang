from flask import Blueprint, jsonify, request
from backend.db_connection import db

analytics = Blueprint("analytics", __name__)

@analytics.route("/analytics", methods=["GET"])
def get_analytics():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM HealthAnalytics;")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@analytics.route("/analytics", methods=["POST"])
def create_analytic():
    data = request.get_json()
    cursor = db.connection.cursor()
    cursor.execute(
        "INSERT INTO HealthAnalytics (profile_id, average_weight, weight_trend, recommended_diet) VALUES (%s, %s, %s, %s)",
        (data["profile_id"], data["average_weight"], data["weight_trend"], data["recommended_diet"])
    )
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Analytic added"}), 201
