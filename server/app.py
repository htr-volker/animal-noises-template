from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    noise = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    animal = requests.get("http://animal_api_type:5000/get_animal").text
    noise = requests.post("http://animal_api_noise:5000/get_noise", data=animal).text
    
    all_animals = Animals.query.order_by(desc(Animals.id)).limit(5).all()

    db.session.add(Animals(type = animal, noise = noise))
    db.session.commit()

    return render_template("index.html", animal=animal, noise=noise, all_animals=all_animals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
