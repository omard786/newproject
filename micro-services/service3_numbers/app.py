import random 
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/numbers", methods=['GET'])
def number_gen():
    number_list = ['1','2','3','4','5','6','7','8', '9']
    random_string = "" 
    for i in range (4):
        random_string += str(random.randint(1,9))
    return random_string
    


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5003, debug= True )

# added the number nine which would decrease the chances of winning 