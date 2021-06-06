from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_height')
def get_height():
    height = random.choice([0.5, 0.55, 0.6, 0.65, 0.7])
    return jsonify({'height':height})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)