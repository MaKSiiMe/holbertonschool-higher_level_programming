#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
     return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_users(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()
    new_user = user.get("username")
    if new_user in users:
        return jsonify({"error": "User already exists"}), 400
    users[new_user] = user
    return jsonify(user), 201


if __name__ == "__main__":
    app.run()
