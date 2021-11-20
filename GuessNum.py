import random


def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'My Guess is {guess}, Is it High(H), Low(L), or Correct one?!\n>>>').upper()
        if feedback == 'H':
            high = guess
        elif feedback == 'L':
            low = guess
    print(f'YAY! I Catch your secret number {guess}! HOORAY...')


guess_computer(1000)