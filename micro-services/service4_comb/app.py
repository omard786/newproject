from flask import Flask, jsonify, json
import requests
import string 
# from flask_sqlalchemy import SQLALchemy
# from flask_wtf import FlaskForm

app = Flask(__name__)




@app.route('/g', methods=['GET'])
def generator():
    # connect = request.get()
    letter_list = requests.get('http://service2_letters:5002/letter').text
    number_list=requests.get('http://service3_numbers:5003/number').text

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
        if int(i)%2 != 0:
            odd_count= odd_count + 1
        elif int(i)%2 ==0:
            even_count=even_count + 1 
#inputting my tariff (conditions)
    prize = "nothing"
    if (vowel_count) >=2 and (even_count) >=2:
        prize = "you have won a gold prize"
    elif (vowel_count) <=2 and (even_count) <=1 or (vowel_count) <=1 and (even_count) <=2 :
        prize = "you have won a silver prize"
    elif  (vowel_count) <=2 or (even_count) <=2:
        prize = "you have won a bronze prize"
        
    packet = {
       "combined_list":combined_list, "vowel_count":vowel_count, "even_count":even_count, "odd_count": odd_count, "prize":prize, 
    }

    return packet



#     if letter_list["vowel_count"] >=2 and number_list["even_count"] >=2:
#         print ("you have won a gold prize")

#     return jsonify(
#         {
#          "letter_list":letter_list, "number_list":number_list
#         }
#     )

# prize_tariff = {
#     "gold": len(even_count) >=2 and len(vowel_count) >=2, 
#     "silver": len()
# }

# j_letter= requests.get('http://localhost:5002/letter')
# data = json.loads(j_letter)
# print(data)
# j_letter= requests.get('http://localhost:5002/letter')
# j_number= requests.get('http://localhost:5003/number')
# print(j_letter.content)
# print(j_number.content)

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


