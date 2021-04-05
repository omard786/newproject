from flask import Flask
import requests

app = Flask(__name__)

@app.route('/comp_gen', methods = ['GET']) 
def comp_gen():
    let_list = requests.get('http://service2_letters:5002/letter_gen')
    num_list = requests.get('http://service3_numbers:5003/number_gen')
    return f'{let_list} {num_list}'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5004, debug=True)