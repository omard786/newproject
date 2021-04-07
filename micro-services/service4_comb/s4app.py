from flask import Flask
import requests

app = Flask(__name__)


@app.route('/generator', methods=['GET'])
def generator():
    letter_list = requests.get('http://service2_letters:5002/letter').text
    number_list=requests.get('http://service3_numbers:5003/number').text


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


