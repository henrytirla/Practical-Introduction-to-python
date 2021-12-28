"""
Write a simple quiz game that has a list of ten questions and a list of answers to those questions. The game should give the player four randomly selected questions to answer. It should
ask the questions one-by-one, and tell the player whether they got the question right or
wrong. At the end it should print out how many out of four they got right.
"""

from enum import Enum
from random import choice

class q_a(Enum):
    QUES_ANS = {'Sky is blue: ':'T', 'Square has 3 sides: ':'F', '100 pennies equal 1 USD dollar: ':'T', 'Leaves can change colors: ':'T', 'Coding sucks: ':'F'}

N = 3 # Number of rounds.
VALID_CHOICE = ['T', 'F']

def quiz_game(N):
    score = 0
    for i in range(N):
        current_ques_ans = get_ques_ans()
        current_ques = unpack_ques(current_ques_ans)
        current_ans = unpack_ans(current_ques_ans)
        valid_user_input = validate_ans(current_ques, current_ans)
        score = check_ans_score(current_ans, valid_user_input, score)
    print(f'\nYour score is {score}.')
    
# Will return a tuple since choosing both items in the dictionary.        
def get_ques_ans():
    ques_ans = choice(list(q_a.QUES_ANS.value.items()))
    return ques_ans

def unpack_ques(current_ques_ans):
    ques = current_ques_ans[0]
    return ques

def unpack_ans(current_ques_ans):
    ans = current_ques_ans[1]
    return ans

def validate_ans(current_ques, current_ans):
    valid = False
    while not valid:
        user_input = input(current_ques)
        user_input = user_input.upper()
        try:
            if user_input in VALID_CHOICE:
                valid = True
            else:
                print('\nYou did not indicate true or false. Please enter "T" or "F".')
        except:
            pass
    return user_input

def check_ans_score(current_ans, valid_user_input, score):
    if current_ans == valid_user_input:
        score += 1
    else:
        pass
    return score
    
def main():
    print('Welcome to True and False Quiz!')
    print('')
    print('Enter "T" if it is true or "F" if it is false.\n')
    quiz_game(N)

if __name__ == '__main__':
    main()
