from flask import Flask, jsonify, json
import requests
from flask_sqlalchemy import SQLALchemy
from flask_wtf import FlaskForm

app = Flask(__name__)




# @app.route('/g', methods=['GET'])
# def generator():
#     letter_list = requests.get('http://service2_letters:5002/letter').json()
#     number_list=requests.get('http://service3_numbers:5003/number').json()
#     return letter_list

# j_letter= requests.get('http://localhost:5002/letter')
# data = json.loads(j_letter)
# print(data)
j_letter= requests.get('http://localhost:5002/letter')
j_number= requests.get('http://localhost:5003/number')
print(j_letter.content)
print(j_number.content)

# @app.route("/service2", methods=['GET']) 
# def service2():
#     let_list = requests.get('http://service2_letters:5002/letter').text
#     return f'{let_list} '


# @app.route("/service3", methods=['GET']) 
# def service3():
#     r_get=requests.get 
#     number_list=r_get('http://service3_numbers:5003/number').text
#     return f'{num_list} '

# @app.route('/frontend')
# def frontend():
#     service2= service2()
#     service3 = service3()
#     return 


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5004, debug=True)


