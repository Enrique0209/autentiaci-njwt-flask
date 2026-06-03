"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager

api = Blueprint('api', __name__)
CORS(api)


# ============ SIGNUP ============
@api.route('/signup', methods=['POST'])
def signup():
    body = request.json
    if body is None:
        return jsonify({"msg": "Request body is empty"}), 400
    if "email" not in body:
        return jsonify({"msg": "Email is required"}), 400
    if "password" not in body:
        return jsonify({"msg": "Password is required"}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=body["email"]).first()
    if existing_user:
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(
        email=body["email"],
        password=body["password"],
        is_active=True
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201


# ============ LOGIN ============
@api.route('/login', methods=['POST'])
def login():
    body = request.json
    if body is None:
        return jsonify({"msg": "Request body is empty"}), 400

    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400

    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({"token": access_token, "user_id": user.id}), 200


# ============ PRIVATE ============
@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user is None:
        return jsonify({"msg": "User not found"}), 404
    return jsonify({"msg": "You are authenticated", "user": user.serialize()}), 200


# ============ HELLO (original) ============
@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }
    return jsonify(response_body), 200