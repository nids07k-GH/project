
import random


def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        return "rock"
    elif choice == '2':
        return "paper"
    elif choice == '3':
        return "scissors"
    else:
        return None


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"


def main():
    print("=== ROCK PAPER SCISSORS GAME ===")

    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()

        print("\nYou chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = decide_winner(user_choice, computer_choice)
        print("Result:", result)

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thank you for playing!")
            break


main()