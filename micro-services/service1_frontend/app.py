from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, request, redirect, jsonify
import requests
app = Flask(__name__)
#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.246.88.163/generator"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_generated= db.Column(db.String(15), nullable=False)
    prize_won = db.Column(db.String(15), nullable=False)
    player_id = db.Column(db.String(15), foreignkey=False)

@app.route('/',methods=['GET', 'POST'])
def home():
    s2_letter = requests.get('http://localhost:5002/numbers').text
    s3_number = requests.get('http://localhost:5003/letters').text
    s4_comb = requests.post('http://localhost:5004/winner',json={"service_numbers":service_two,"service_letters":service_three}).text
    prize_given = prize( number_generated= s4_comb["combined_list"], prize_won = s4_comb["prize"])
    db.session.add(prize_given)
    db.session.commit()
    return render_template('home.html', number_generated= s4_comb["combined_list"], prize_won = s4_comb["prize"])


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
