from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_animal', methods=['GET'])
def get_animal():
    return random.choice(["pig", "cow", "horse", "chicken", "sheep", "shark"])

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)