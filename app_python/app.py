from datetime import datetime
from flask import Flask, jsonify
import pytz
import os

app = Flask(__name__)
timezone = pytz.timezone(os.environ.get('TZ', 'Europe/Moscow'))

path = os.path.join(os.environ.get('DATA_DIR', '/'), 'output.txt')


@app.route("/")
def index():
    output = {
        "local time": str(datetime.now().astimezone(timezone)),
        "utc time": str(datetime.now()),
    }
    with open(path, 'a') as f:
        f.write(str(output))
    return jsonify(output)


@app.route("/visits")
def visits():
    if os.path.exists(path):
        with open(path, 'r') as f:
            output = f.read()
            return output
    else:
        return 'No visits'


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
    )
