# str, str -> void
def RPSgame(player1, player2):
    """Prints outcome of one round of the rock, paper, scissors game.
       This function uses the function isLegal and beats, which you
       have to write"""
    if not (isLegal(player1) and isLegal(player2)):
        print("Both players must select from rock, paper, or scissors")
    elif beats(player1, player2):
        print("Player 1 wins")
    elif beats(player2, player1):
        print("Player 2 wins")
    else:
        print("It's a tie")


#str->str
def isLegal(weapon):
    """This function decides whether the user's weapon input is on list of valid weapons"""
    if (weapon == "rock" or weapon ==  "paper" or weapon == "scissors"):
        return True
    else:
        return False
        
#str->str
def beats(p1, p2):
    """This function determines who would win in a battle between the two weapons chosen from player1 and player 2"""
    if ((p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper") or (p1 == "rock" and p2 == "scissors")):
        return True
    else:
        return False
    
    
        



