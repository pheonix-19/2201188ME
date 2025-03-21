from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "http://20.244.56.144/test"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    response = requests.post(f"{BASE_URL}/register", json=data).json()
    return jsonify(response)



if __name__ == "__main__":
    app.run(debug=True)