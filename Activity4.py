"""
Using Loops:
  Enhance the previously written Rock-Paper-Scissors code so that it asks the user if they want to play another round.
     If they say 'Yes', the game should begin again.
     If they say 'No', the game should exit.

"""
# Get the users names
U1=input("Enter player1 Name: ")
U2=input("Enter player2 Name: ")

while True :	
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

    # Get the users choices
    Play_again1 = input(U1 + ", do you want to play again ").lower()
    Play_again2 = input(U2 + ", do you want to play again ").lower()

    if (Play_again1 == 'yes' and Play_again2 == 'yes'):
        pass
    elif (Play_again1 == 'no' and  Play_again2 == 'no'):
        raise SystemExit
    else:
        print("Invalid Input. Exiting the flow")
        raise SystemExit
