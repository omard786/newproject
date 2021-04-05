import random 
from flask import Flask

app = Flask(__name__)


@app.route("/number_gen")
def number_gen():
    number_list = ['1','2','3','4','5','6','7','8']
    even = '2468'
    odd = '1357'
    #choices let you pick the letters from the lise, k=amount of objects from the list, weights is the prob of occuring  
    number= random.choices(number_list, weights=[1, 1, 1, 1, 1, 1, 1, 1], k=4)

    # print('these are your numbers :')
    dash_list_num= '-'.join(number)

    #list comphrension, using one list with another 
    even_count = [i for i in number if i in even]
    # print ('you have this many even numbers : ', len(even_count))
    odd_count = [i for i in number if i in odd]
    # print ('you have this many odd numbers : ', len(odd_count))
    return f"{len(even_count)} {len(odd_count)} {dash_list_num}"



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5003, debug= True )
