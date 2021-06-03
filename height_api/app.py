from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_height')
def get_height():
    height = random.choice([1.524,1.626,1.7272,1.8034,1.880,1.93,2.007])
    return jsonify({'height':height})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)