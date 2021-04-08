class player_reg(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(15), nullable=False)

class prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_generated= db.Column(db.String(15), nullable=False)
    prize_won = db.Column(db.String(15), nullable=False)
    player= db.relationship('player_reg', backref = 'prize')