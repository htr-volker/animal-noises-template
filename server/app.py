from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)


class Humans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float,nullable=False)
    weight = db.Column(db.Float,nullable=False)
    size = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    height = requests.get('http://height_api:5000/get_height')
    weight = requests.get('http://weight_api:5000/get_weight')
    result = {**height.json(),**weight.json()}
    size = requests.post('http://bmi_api:5000/get_bmi', json=result)

    last_five_humans = Humans.query.order_by(Humans.id.desc()).limit(5).all()

    db.session.add(
        Humans(
            height = height.json()['height'],
            weight = weight.json()['weight'],
            size= size.text
        )
    )
    db.session.commit()

    return render_template('index.html', height=height.json()['height'], weight=weight.json()['weight'], size=size.text, last_five_humans = last_five_humans)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)