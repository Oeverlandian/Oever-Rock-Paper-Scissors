import random

def main_menu():
    """Displays the main menu and handles user choice."""
    while True:
        print("Which type of Rock-Paper-Scissors do you want to play?")
        print("1. Rock-Paper-Scissors")
        print("2. Rock-Paper-Scissors-Well (Not available yet)")
        print("3. Rock-Paper-Scissors-Fire-Water (Not available yet)")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            play_rock_paper_scissors()
        elif choice == '2':
            print("Rock-Paper-Scissors-Well is not available yet.")
        elif choice == '3':
            print("Rock-Paper-Scissors-Fire-Water is not available yet.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def get_computer_choice():
    """Gets the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def play_rock_paper_scissors():
    """Handles the Rock-Paper-Scissors game logic."""
    while True:
        print("\nWhat do you choose?")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Return to menu")

        player_choice = input("Enter your choice: ").strip().lower()

        if player_choice in ['1', 'rock']:
            player_choice = 'rock'
        elif player_choice in ['2', 'paper']:
            player_choice = 'paper'
        elif player_choice in ['3', 'scissors']:
            player_choice = 'scissors'
        elif player_choice in ['4', 'return to menu', 'return']:
            return
        else:
            print("Invalid input. Please choose 1, 2, 3, or 4.")
            continue

        computer_choice = get_computer_choice()

        if player_choice == computer_choice:
            print(f"You chose {player_choice} and the computer chose {computer_choice}. It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
        else:
            print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")

        if not play_again():
            print("Returning to the main menu.")
            return

def play_again():
    """Asks the user if they want to play again."""
    while True:
        choice = input("Do you want to play again? (Y/N): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

if __name__ == "__main__":
    main_menu()

#End of program