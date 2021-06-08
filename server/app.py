from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# db = SQLAlchemy(app)



# db.create_all()

@app.route('/')
def home():
    animal = requests.get("http://animal_api:5000/get_animal").text
    noise = requests.post("http://animal_api:5000/get_noise", data=animal).text
    
    return render_template("index.html", animal=animal, noise=noise, animals=animals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
