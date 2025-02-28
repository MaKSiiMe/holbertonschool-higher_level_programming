#!/usr/bin/python3

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.login_required
def get_users():
    return jsonify(users)

@app.route('/login', methods=['POST'])

