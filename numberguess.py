import random


answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))

guess = int(input('Guess the number(1-100): '))
print(guess, type(guess))

if guess-answer==0:
    print('Correct!')
elif guess<answer:
        print('Up!')
elif guess>answer:
        print('Down!')
        
print('Wrong! The answer was {}.'.format(answer))
