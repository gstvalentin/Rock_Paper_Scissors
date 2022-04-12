def winner(player, opponent):
    if (player == 1 and opponent == 3) or (player == 3 and opponent == 2) or (player == 2 and opponent == 1):
        return True
        
print(winner(1,3))
