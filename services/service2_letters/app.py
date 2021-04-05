import random 

letter_list = ['A','E','I','U','B','F','J','V']
vowels = 'AEIU'
consonant = 'BFJV'
#choices let you pick the letters from the lise, k=amount of objects from the list, weights is the prob of occuring  
letter= random.choices(letter_list, weights=[1, 1, 1, 1, 1, 1, 1, 1], k=4)

print('these are your letters :')
dash_list= print('-'.join(letter))

#sort it so the letters dont reproduce 


#list comphrension, using one list with another 
vowel_count = [i for i in letter if i in vowels]
print ('you have this many vowels : ', len(vowel_count))

consonant_count = [i for i in letter if i in consonant]
print ('you have this many consonants : ', len(consonant_count))