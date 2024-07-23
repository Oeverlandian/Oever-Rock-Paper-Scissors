import random

def returnToChoose():
    chooseType()

def chooseType():
    """Prompts the user to choose a type of Rock Paper Scissors game."""

    print("Which type of rock paper scissors do you want to play?")
    print("1. Rock-Paper-Scissors")
    print("2. Rock-Paper-Scissors-Well (Not available yet)")
    print("3. Rock-Paper-Scissors-Fire-Water (Not available yet)")

    while True:
        choice = input().strip()

        if choice == '1':
            computerChoiceRPS()
            rockPaperScissors()
            break
        elif choice == '2':
            print("Rock-Paper-Scissors-Well is not available yet.")
        elif choice == '3':
            print("Rock-Paper-Scissors-Fire-Water is not available yet.")
        else:
            print("That is not a valid number, input a number from 1 to 3")

def computerChoiceRPS():
    computerInt = random.randint(1,3)
    if computerInt == 1:
        computerChoiceRPS = 1
        
def rockPaperScissors():
    while True:
        print("""What do you choose?
            1. Rock
            2. Paper
            3. Scissors
            4. Return back to menu
            """)
        playerChoice = input().strip().lower()
        
        #tied outcomes
        if (playerChoice == 1 or playerChoice == 'rock') and (computerChoiceRPS == 1 or computerChoiceRPS == 'rock'):
            print("You chose rock and the computer chose rock, you tied!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()
        elif (playerChoice == 2 or playerChoice == 'paper') and (computerChoiceRPS == 2 or computerChoiceRPS == 'paper'):
            print("You chose scissors and the computer chose scissors, you tied!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()
        elif (playerChoice == 3 or playerChoice == 'scicssors') and (computerChoiceRPS == 2 or computerChoiceRPS == 'scissors'):
            print("You chose scissors and the computer chose scissors, you tied!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()

        #winning outcomes
        elif (playerChoice == 1 or playerChoice == 'rock') and (computerChoiceRPS == 3 or computerChoiceRPS == 'scissors'):
            print("You chose rock and the computer chose scissors, you won!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()
        elif (playerChoice == 2 or playerChoice == 'paper') and (computerChoiceRPS == 1 or computerChoiceRPS == 'rock'):
            print("You chose paper and the computer chose rock, you won!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()
        elif (playerChoice == 3 or playerChoice == 'scissors') and (computerChoiceRPS == 2 or computerChoiceRPS == 'paper'):
            print("You chose scissors and the computer chose paper, you won!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()

        #losing outcomes
        elif (playerChoice == 1 or playerChoice == 'rock') and (computerChoiceRPS == 2 or computerChoiceRPS == 'paper'):
            print("You chose rock and the computer chose paper, you lost!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()
        elif (playerChoice == 2 or playerChoice == 'paper') and (computerChoiceRPS == 3 or computerChoiceRPS == 'scissors'):
            print("You chose rock and the computer chose paper, you lost!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()
        elif (playerChoice == 3 or playerChoice == 'rock') and (computerChoiceRPS == 1 or computerChoiceRPS == 'paper'):
            print("You chose rock and the computer chose paper, you lost!")
            #return to menu choice
            print("Do you want to return to the menu? Y/N")
            returnChoice = input().strip().lower()
            if returnChoice == "y" or "yes":
                print("Returning you to the main menu!")
                returnToChoose()
            if returnChoice == "n" or "no":
                print("Terminating program.")
                exit()

        #return to menu
        elif playerChoice == 4 or "return" or "return back to menu":
            chooseType()

        #error
        else:
            print("Invalid input or error.")
            print("Do you want to return to the start of the RPS game? Y/N")
            rerun = input().strip().lower()
            if rerun == "y" or "yes":
                print("Restarting program.")
                rockPaperScissors()
            elif rerun == "n" or "no":
                print("Terminating program")
                exit()
            else:
                print("Invalid input, terminating program.")
                exit()
    
#WIP def rockPaperScissorsWell():

#WIP def rockPaperScissorsFireWater():

chooseType()