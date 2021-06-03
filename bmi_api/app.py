from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_bmi', methods=['POST'])
def get_bmi():
    height = request.json['height']
    weight = request.json['weight']   
    bmi = (weight/(height**2))
    if bmi <18.5:
        size="underweight"
    elif bmi >18.5 and bmi<24.9:
        size = "healthyweight"
    elif bmi>24.9:
        size="overweight"
    return size

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)