import random


def guess(x):
    """Defines a random number and allows you to guess"""
    random_number = random.randint(0, x)
    guess = -1
    while guess != random_number:
        guess = int(input(f'Number is between 0 and {x}: '))
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')
    print(f'Ez win, number is {random_number}')


print(guess.__doc__)
guess(10)
