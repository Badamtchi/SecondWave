import random
wep = {'P':'Paper', 'S':'Scissors', 'R':'Rock'}


def play():
    user = ''
    while user != 'Q':
        user = input('Pick one;\n(R) for Rock,\n(P) for Paper,\n(S) for Scissors,\n(Q) for Quit\n>>> ').upper()
        computer = random.choice(['R', 'P', 'S'])

        if user == computer:
            return f"It's a tie!\n...We both took {wep[user]}!!!"

        if is_win(user, computer):
            return f"YOU WON!\n... You picked {wep[user]} and I {wep[computer]}!\nCongratulation"
        return f"YAY!!! YOU LOST!\nBecause You took {wep[user]} but I choose {wep[computer]}..."


def is_win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'P' and opponent == 'R') \
            or (player == 'S' and opponent == 'P'):
        return True

print(play())
