import random

def play():
    user = input("Choose an option: r for rock, p for paper, s for scissors.\n").lower()
    dict_option = {'r':'rock', 'p': 'paper', 's':'scissors'}
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'It was a draw! You and the computer choosed {dict_option[computer]}'

    if win_the_user(user, computer):
        return f'You won! You choosed {dict_option[user]} and the computer choosed {dict_option[computer]}'

    return f'You lost! You choosed {dict_option[user]} and the computer choosed {dict_option[computer]}'


def win_the_user(player1, player2):
    # It returns TRUE if
    #  r > s
    #  s > p
    #  p > r
    if ((player1 == 'r' and player2 == 's')
       or (player1 == 's' and player2 == 'p')
       or (player1 == 'p' and player2 == 'r')):
       return True
    return False

print(play())