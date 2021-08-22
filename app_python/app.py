from datetime import datetime
from flask import Flask, jsonify
import pytz
import os

app = Flask(__name__)
timezone = pytz.timezone(os.environ.get('TZ', 'Europe/Moscow'))


@app.route("/")
def index():
    print(datetime.now().astimezone(timezone))
    return jsonify({
        "local time": str(datetime.now().astimezone(timezone)),
        "utc time": str(datetime.now()),
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
    )
