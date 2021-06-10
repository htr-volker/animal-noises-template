from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_noise', methods=['POST'])
def get_noise():
    noises = {
        "pig" : "oink",
        "cow" : "moo",
        "horse" : "neigh",
        "chicken" : "cluck",
        "sheep" : "baa",
        "shark" : "dun dunn"
    }
    return noises[request.data.decode('utf-8')]

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)