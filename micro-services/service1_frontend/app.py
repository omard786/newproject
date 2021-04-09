# from wtforms import StringField, SubmitField
from flask import Flask, request, Response, redirect, jsonify, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@34.89.15.126/generator"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_generated= db.Column(db.String(15), nullable=False)
    prize_won = db.Column(db.String(150), nullable=False)

@app.route("/home", methods=['GET', 'POST'])
def home():
    s2_letter = requests.get('http://service2_letters:5002/letters').text
    s3_number = requests.get('http://service3_numbers:5003/numbers').text
    s4_comb = requests.post('http://service4_comb:5004/generator',json={"service2_letter":s2_letter,"service3_numbers":s3_number}).json()
    prize_given = prize(number_generated= s4_comb["combined_list"], prize_won = s4_comb["prize"])
    db.session.add(prize_given)
    db.session.commit()
    return render_template('home.html', title='prize', number_generated= s4_comb["combined_list"], prize_won = s4_comb["prize"])


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
