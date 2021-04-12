import random 
from flask import Flask , jsonify
import string 

app = Flask(__name__)


@app.route("/letters", methods=['GET'])
def letter_gen():
    letter_list = ['A','E','I','U','B','F','J','V']
    random_string = "".join(random.choice(letter_list) for i in range(4))
    return random_string

    return jsonify(package) 
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5002, debug= True )

