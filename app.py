from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "hello"})


if __name__ == "__main__":
    app.run(debug=True)
