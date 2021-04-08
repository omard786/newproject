from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, request, redirect



class registrationform(FlaskForm):
    first_name = StringField('first name')
    last_name = StringField('last name')
    age = StringField('age')
    submit = SubmitField('sign up')


@app.route('/sign_up', methods=['GET', 'POST']) 
#@app.route('/home', methods=['GET', 'POST'])
def sign_up():
    error=""
    form=registrationform()
    #this ensures the data from the website is transmitted to database 
    if(request.method=='POST'):
        firstname=form.first_name.data
        lastname=form.last_name.data
        age = form.age.data
        #this doesnt let the fields be empty 
        if len(firstname) == 0 or len(lastname) == 0 or len(age) == 0:
            error="please fill in all fields"
        else:
        
                new_player = models.player_reg(first_name=firstname, last_name=lastname, age=age)
                db.session.add(new_player)
                db.session.commit()
            return redi