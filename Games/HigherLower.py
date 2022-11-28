#import the data
#access the data by writing a function that returns the required value
#data[data1][0]=name, data[data2]=follower count and so on.
#name, description and country need to be out putted while asking for choice
#ask the user to choose
#get the input save it
#compare the choices
##correct if the userchoice > other choice
##print result and continue to loop
##if wrong end the game and output a value based on correct guesses as score

from HigherLowergamedata import data
from random import randint

vs="\nvs\n"

CORRECT = True

n=0


def print_question(a,b):
        '''returns a value of given key'''
    
        name = data [a]['name']
        description = data [a]['description']
        country = data[a]['country']
        optionA = f"A. {name} is a {description} from {country}"
        print(optionA)
        
        print(vs)
        
        name = data [b]['name']
        description = data [b]['description']
        country = data[b]['country']
        optionB = f"B. {name} is a {description} from {country}"
        print(optionB)

while CORRECT:
    #Random A values   

    print('WHO HAS MORE FOLLOWERS?\n')
    A = randint(0, len(data)-1)
    B = randint(0, len(data)-1)

    while A==B:
        B = randint(0, len(data)-1)
    
    print_question(A, B)

    u = input('A or B? : ')

    if u=='A' and A<B:
        print('CORRECT\n')
    elif u=='B' and B<A:
        print('CORRECT\n')
    else:
        print('WRONG\n')
        CORRECT = False
        print(f'your score {n}\n')
    
    n=n+1

    print(f"{data[A]['name']} has {data[A]['follower_count']} million followers\n")
    print(f"{data[B]['name']} has {data[B]['follower_count']} million followers\n\n")