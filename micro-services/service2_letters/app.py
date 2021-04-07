import random 
from flask import Flask , render_template, jsonify

app = Flask(__name__)


@app.route("/letter", methods=['GET'])
def letter_gen():
    letter_list = ['A','E','I','U','B','F','J','V']
    vowels = 'AEIU'
    consonant = 'BFJV'
    #choices let you pick the letters from the lise, k=amount of objects from the list, weights is the prob of occuring  
    letter= random.choices(letter_list, weights=[1, 1, 1, 1, 1, 1, 1, 1], k=4)

    #puts dash (-) in list to separate 
    dash_list_let='-'.join(letter)

    #sort it so the letters dont reproduce 


    #list comphrension, using one list with another 
    vowel_count = [i for i in letter if i in vowels]
    consonant_count = [i for i in letter if i in consonant]
    package = { 
        "vowel_count": len(vowel_count), "consonant_count": len(consonant_count) , "dash_list_let": dash_list_let
    }
    return jsonify(package) 
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5002, debug= True )

