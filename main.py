import requests
import os
import random
# Import temporary word lists
from word_list import words
# Arbitraty numbers of max attempts
TOTAL_ATTEMPTS = 7

# Set apikey to the APIKEY in the environment variables
# apikey = os.environ["API_KEY"]
# Print the key to check is works
# print(apikey)
# api_url = ''
# data = requests.get(api_url).json()

def choose_random_word():
    selected_word = random.choice(words)
    while (("-" or " ") in selected_word):
        selected_word = random.choice(words)
    return selected_word

def present_game_status(presented_word, current_attempts, attempted_letters):
    print("|----------------------------------------")
    print(f"| Number of wrong attempts: {current_attempts}/{TOTAL_ATTEMPTS}")
    print(f"| Word : {presented_word}")
    print(f"| Attempted letters : {attempted_letters}")
    print("|----------------------------------------")

# User entered max attempts
def is_game_lost(current_attempts):
    return current_attempts == TOTAL_ATTEMPTS

def is_game_won(presented_word, selected_word):
    return presented_word == selected_word

def find_index_letter_in_word(user_letter, selected_word):
    return [i for i, letter in enumerate(selected_word) if letter == user_letter]

def replace_letter_in_word(index, user_letter, presented_word):
    return presented_word[:index] + user_letter + presented_word[index + 1:]

def main():
    # Select the word to guess
    selected_word = choose_random_word().lower()
    # Create presented word with "_" for the user to guess
    presented_word = "_" * len(selected_word)
    # Current numbers of attempts by user
    current_attempts = 0
    # List of attempted letters
    attempted_letters = []
    print(f"Chosen word {selected_word}")

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
            # Can only be one single character
            if len(user_letter) != 1:
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
                current_attempts += 1

if __name__ == "__main__":
    main()