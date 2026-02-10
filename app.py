from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "hello"})


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return jsonify({"ok": True, "timestamp": timestamp})


if __name__ == "__main__":
    app.run(debug=True)
