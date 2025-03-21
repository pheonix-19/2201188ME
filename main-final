from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "http://20.244.56.144/test"
def get_headers():
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        return None
    return {"Authorization": token}

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    response = requests.post(f"{BASE_URL}/register", json=data).json()
    return jsonify(response)

@app.route("/auth", methods=["POST"])
def authenticate():
    data = request.json
    response = requests.post(f"{BASE_URL}/auth", json=data).json()
    return jsonify(response)

@app.route("/users", methods=["GET"])
def get_users():
    print(request.headers)  
    headers = get_headers()
    if not headers:
        return jsonify({"message": "An authorization header is required"}), 401
    response = requests.get(f"{BASE_URL}/users", headers=headers).json()
    return jsonify(response)

@app.route("/users/<int:user_id>/posts", methods=["GET"])
def get_user_posts(user_id):
    headers = get_headers()
    if not headers:
        return jsonify({"message": "An authorization header is required"}), 401
    response = requests.get(f"{BASE_URL}/users/{user_id}/posts", headers=headers).json()
    return jsonify(response)

@app.route("/posts/<int:post_id>/comments", methods=["GET"])
def get_post_comments(post_id):
    headers = get_headers()
    if not headers:
        return jsonify({"message": "An authorization header is required"}), 401
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments", headers=headers).json()
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)



