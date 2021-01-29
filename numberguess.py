import random


answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))
chance = 3

while chance > 0:
    guess = int(input('Guess the number(1-100): '))
    print(guess, type(guess))

    if guess-answer==0:
        print('Correct!')
        break
    elif guess<answer:
        msg = 'Up!'
    elif guess>answer:
        msg = 'Down!'
    chance-=1
    print('{} You have {} life(s).'.format(msg, chance))
    
    if chance ==0:
        print('You now dead! The answer was {}.'.format(answer))

