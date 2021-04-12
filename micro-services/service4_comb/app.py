from flask import Flask, Response, jsonify, json
import requests
import string 

app = Flask(__name__)

@app.route('/generator', methods=['GET', 'POST'])
def generator():
    # connect = request.get()
    letter_list = requests.get('http://service2_letters:5002/letters').text
    number_list=requests.get('http://service3_numbers:5003/numbers').text
    app.logger.info(str(number_list))

    combined_list = letter_list + number_list
    vowel_count = 0 
    even_count = 0 
    odd_count = 0 
    if ("A" in letter_list):
        vowel_count = vowel_count + 1
    if ("E" in letter_list): 
        vowel_count = vowel_count + 1
    if ("I" in letter_list):
        vowel_count = vowel_count + 1
    if ("U" in letter_list):
        vowel_count = vowel_count + 1
    for i in number_list:
        if int(i)%2 != 0 :
            odd_count= odd_count + 1
        elif int(i)%2 == 0 :
            even_count=even_count + 1 
#inputting my tariff (conditions)
    prize = "nothing"
    if (vowel_count) >=2 and (even_count) >=2:
        prize = "you have won a platinum prize"
    elif (vowel_count) <=2 and (even_count) <=1 or (vowel_count) <=1 and (even_count) <=2 :
        prize = "you have won a gold prize"
    elif  (vowel_count) <=2 or (even_count) <=2:
        prize = "you have won a silver prize"

    return jsonify({
       "combined_list":combined_list, "vowel_count":vowel_count, "even_count":even_count, "odd_count": odd_count, "prize":prize,  
    })


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5004, debug=True)


#change the prizes to reflect that it is now harder to win the top prize 