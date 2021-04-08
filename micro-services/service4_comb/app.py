from flask import Flask, jsonify, json
import requests
# from flask_sqlalchemy import SQLALchemy
# from flask_wtf import FlaskForm

app = Flask(__name__)




@app.route('/g', methods=['GET'])
def generator():
    letter_list = requests.get('http://service2_letters:5002/letter').json()
    number_list=requests.get('http://service3_numbers:5003/number').json()

  #inputting my tariff
    prizes:
        if letter_list.count(vowel_count) >=2 and number_list.count(even_count) >=2:
        print("you have won a gold prize")
        elif:
        letter_list.count(vowel_count) <=2 and number_list.count(even_count) =1 or letter_list.count(vowel_count) <=1 and number_list.count(even_count) =2:
        print("you have won a silver prize")
        elif: letter_list.count(vowel_count) <=2 or number_list.count(even_count) <=2:
        print("you have won a bronze prize")
        s4_gen = {
         "letter_list":letter_list, "number_list":number_list, 
        }



    if letter_list["vowel_count"] >=2 and number_list["even_count"] >=2:
        print ("you have won a gold prize")

    return jsonify(
        {
         "letter_list":letter_list, "number_list":number_list
        }
    )

prize_tariff = {
    "gold": len(even_count) >=2 and len(vowel_count) >=2, 
    "silver": len()
}

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


