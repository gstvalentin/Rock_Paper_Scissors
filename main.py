
from random import randint
import re

def play():
    wanna_play = input('\nDo you wanna play ROCK, PAPER OR SCISSOR? [Y/N]: ')
    wplay = wanna_play.lower()
    #print(wplay)

    computer = randint(1,3)
    if wplay == 'y':
        wplay = True
    elif wplay == 'n':
        wplay = False
    while type(wplay) != type(bool(True)):
        print('\nPlease choose Y or N!')
        wanna_play = input('Do you wanna play ROCK, PAPER OR SCISSOR? [Y/N]: ')
        wplay = wanna_play.lower()
        if wplay == 'y':
            wplay = True
        elif wplay == 'n':
            wplay = False
    
    if wplay:
        user = int(input('\n[01] FOR ROCK\n[02] FOR PAPER\n[03] FOR SCISSOR\nTell me your choice: '))
        #?digitar algo diferente try except
    
    if user == computer:
        print('It\'s a Draw')
        play_again = input('Wanna play again? [Y/N]  ')
        
    print(user, computer)
    if winner(user, computer):
        print('You Won!')
        return True
    
    return print('You Lost!')
    
def winner(player, opponent):
        if (player == 1 and opponent == 3) or (player == 3 and opponent == 2) or (player == 2 and opponent == 1):
            return True

play()
