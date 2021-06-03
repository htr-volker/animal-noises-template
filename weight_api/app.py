from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_weight')
def get_weight():
    weight = random.choice([40,50,60,70,80,90,100])
    return jsonify({'weight':weight})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)