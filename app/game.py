



from random import choice

#
# USER SELECTION
#alid_input = ["rock", "paper", "scissors"]
#
# = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
#rint("USER CHOICE:", u)
#f u not in valid_input:
#   print("OOPS, TRY AGAIN")
#   exit()
#
#
# COMPUTER SELECTION
#
#
# = choice(valid_input)
#rint("COMPUTER CHOICE:", c)
#
#
# DETERMINATION OF WINNER
#
#
#if u == "rock" and c == "rock":
#    print("It's a tie!")
#elif u == "rock" and c == "paper":
#    print("The computer wins")
#elif u == "rock" and c == "scissors":
#    print("The user wins")
#
#elif u == "paper" and c == "rock":
#    print("The computer wins")
#elif u == "paper" and c == "paper":
#    print("It's a tie!")
#elif u == "paper" and c == "scissors":
#    print("The user wins")
#
#elif u == "scissors" and c == "rock":
#    print("The computer wins")
#elif u == "scissors" and c == "paper":
#    print("The user wins")
#elif u == "scissors" and c == "scissors":
#    print("It's a tie!")
#
def determine_winner(user_choice, computer_choice):
    """
    This is a docstring. It tells us who the winner is. It takes inputs "rock" "paper" or "scissors"
    and will return a winner between the computer and the user. 


    Example: determine_winner("rock", "paper")
    """
    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice

if __name__ == "__main__":
    valid_selections = ["rock", "paper", "scissors"] # only have to update in one place
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_selections:
        print("OOPS, TRY AGAIN")
        exit()
    c = choice(valid_selections)
    print("COMPUTER CHOICE:", c)
    winner = determine_winner(u,c)
    if winner == u:
        print("YOU WON")
    elif winner == c:
        print("COMPUTER WON")
    else:
        print("TIE")