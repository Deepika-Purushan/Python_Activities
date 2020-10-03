"""
    Make a two-player Rock-Paper-Scissors game.
    Remember the rules:
        Rock beats scissors
        Scissors beats paper
        Paper beats rock
"""
# Get the users names
U1=input("Enter player1 Name: ")
U2=input("Enter player2 Name: ")
	
# Get the users choices
Player1_answer = input(U1 + ", do you want to choose rock, paper or scissors? ").lower()
Player2_answer = input(U2 + ", do you want to choose rock, paper or scissors? ").lower()
print(Player1_answer)
print(Player2_answer)
	
# Run the algorithm to see who win	
if Player1_answer == Player2_answer:	
    print("It's a tie!")	
elif Player1_answer == 'rock':	
    if Player2_answer == 'scissors':	
        print("Rock wins!")	
    else:	
        print("Paper wins!")
elif Player1_answer == 'scissors':
    if Player2_answer == 'paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
elif Player1_answer == 'paper':
    if Player2_answer == 'rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")