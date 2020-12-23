import sys
import random
# Import temporary word lists
from word_list import words
# Arbitraty numbers of max attempts
TOTAL_ATTEMPTS = 7

def choose_random_word():
    selected_word = random.choice(words)
    while (("-" or " ") in selected_word):
        selected_word = random.choice(words)
    return selected_word

def present_game_status(presented_word, current_attempts, attempted_letters):

    print("|----------------------------------------")
    print(f"| Word : {presented_word}")
    print("| Attempted letters :", *attempted_letters, sep=" ")
    print(f"| Wrong attempts left : {current_attempts}/{TOTAL_ATTEMPTS}")
    print("|----------------------------------------")

def show_actions_menu():
    print("|----------- POSSIBLE ACTIONS -----------")
    print("| p - Start a game")
    print("| h - Help")
    print("| q - Quit game")
    print("|----------------------------------------")

def show_help_menu():
    print("|------------- HOW IT WORKS -------------")
    print("| Guess a word within a number of")
    print("| attempts (7). Input a single letter to")
    print("| see if it is in the word.")
    print("|----------------------------------------")

def show_wrong_input():
    print("Wrong action!")
    show_actions_menu()

# User entered max attempts
def is_game_lost(current_attempts):
    return current_attempts == TOTAL_ATTEMPTS

# User has guessed the word
def is_game_won(presented_word, selected_word):
    return presented_word == selected_word

# Find all occurrences of the input letter
def find_index_letter_in_word(user_letter, selected_word):
    return [i for i, letter in enumerate(selected_word) if letter == user_letter]

# Replace all occurences of the input letter into presented word
def replace_letter_in_word(index, user_letter, presented_word):
    return presented_word[:index] + user_letter + presented_word[index + 1:]

def validate_user_input(user_letter):
    # Can only be one single character
    if len(user_letter) != 1:
        print(f"Sequence {user_letter} is not a single letter")
        return False
    if user_letter.isalpha() == False:
        print(f"Character {user_letter} is not a letter")
        return False
    return True

def run_game():
    # Select the word to guess
    selected_word = choose_random_word().lower()
    # Create presented word with "_" for the user to guess
    presented_word = "_" * len(selected_word)
    # Current numbers of attempts by user
    current_attempts = 0
    # List of attempted letters
    attempted_letters = []

    # Game loop
    while(True):
        # Check if game is over
        if(is_game_lost(current_attempts)):
            present_game_status(selected_word,current_attempts,attempted_letters)
            print(f"You lost !")
            return
        elif(is_game_won(presented_word,selected_word)):
            present_game_status(selected_word,current_attempts,attempted_letters)
            print(f"You won !")
            return
        # Or to continue
        else:
            # Print current status to user
            present_game_status(presented_word, current_attempts, attempted_letters)
            # Ask user a letter to try
            user_letter = input("Choose a letter : ").lower()
            # Validate the input
            if validate_user_input(user_letter) == False:
                continue
            # Letter was already attempted
            if user_letter in attempted_letters:
                print(f"Letter {user_letter} was already attempted")
                continue
            # Add letter to attempted letters
            attempted_letters.append(user_letter)
            # Letter is in the selected word
            if user_letter in selected_word:
                letter_indexes = find_index_letter_in_word(user_letter, selected_word)
                for index in letter_indexes:
                    presented_word = replace_letter_in_word(index, user_letter, presented_word)
            else:
                # Letter is not in selected word
                current_attempts += 1

def main():
    print("Welcome to Hangman !")
    show_actions_menu()

    while(True):
        action = input()

        # Verify if user wants to quit
        if str(action).lower() == "q":
            # Quit game
            print("Thanks for playing!")
            sys.exit()

        # Show help menu
        if str(action).lower() == "h":
            show_help_menu()
            continue

        # Start game
        if str(action).lower() == "p":
            run_game()
        
        # Not a valid input
        else:
            show_wrong_input()

if __name__ == "__main__":
    main()