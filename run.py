from random import randrange
import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman_categories")
CATEGORIES = SHEET.worksheet("categories")


def select_difficluty():
    """
    Request for user to select game difficulty: Hard (5 Lives),
    Medium (6 Lives), Easy (7 Lives)
    """
    print("Please select your game difficulty.\n")

    game_difficulty = {"Hard": 5, "Medium": 6, "Easy": 7}

    num = 1

    for difficulty, lives in game_difficulty.items():
        print(f"{num} - {difficulty} ({lives} Lives)")
        num += 1

    print("")
    input_value = int(input("Which difficulty would you like to select? "))
    input_value -= 1

    difficulty = list(game_difficulty)[input_value]
    lives = list(game_difficulty.values())[input_value]

    os.system('cls||clear')
    print("")
    print(f"You have selected game difficulty {difficulty} and will have {lives} lives.\n")

    return lives


def select_category():
    """
    Request for user to select the game category or for a random category to
    be chosen
    """
    print("Please select one of the following categories, or choose 'Random' if you would like us to pick one for you.\n")

    data = CATEGORIES.get_all_values()
    categories_row = data[0]

    num = 1

    for category in categories_row:
        print(f"{num} - {category}")
        num += 1

    print(f"{num} - Random\n")

    category_input = int(input("Which category number would you like to select? "))
    category_column = category_input - 1

    if category_input <= len(categories_row):
        os.system('cls||clear')
        print("")
        print(f"You have chosen to guess something related to {categories_row[category_column]}.\n")
    else:
        category_column = randrange((len(categories_row)))
        os.system('cls||clear')
        print("")
        print(f"The random category selected for you is {categories_row[category_column]}.\n")

    category_column += 1

    return category_column


def retrieve_word(column):
    """
    Retrieve word, phrase or sentence from the selected category column
    """
    column_values = CATEGORIES.col_values(column)
    column_values.pop(0)
    rand_column_cell = randrange((len(column_values)))
    game_word = column_values[rand_column_cell]
    # game_word.upper()

    final_game_word = []

    for letter in list(game_word):
        if letter == " ":
            letter = "/"
            final_game_word.append(letter)
        else:
            final_game_word.append(letter)

    game_word = ''.join(final_game_word)
    return game_word


def hide_game_word(game_word):
    """
    Change the game word into dashes (-, letters) and slashes (/, spaces)
    ready for the player to guess
    """
    game_word_split = list(game_word)

    hide_word = []

    for letter in game_word_split:
        if letter != "/":
            letter = "-"
            hide_word.append(letter)
        else:
            hide_word.append("/")

    hidden_game_word = ""

    for letter in hide_word:
        hidden_game_word += letter

    return hidden_game_word


class Game:
    """
    Main game play class
    """
    # Class variable
    # alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self, letter_guess, game_word, hidden_game_word, lives):
        self.letter_guess = letter_guess
        self.game_word = game_word
        self.hidden_game_word = hidden_game_word
        self.lives = lives

    def check_game_word(self):
        """
        Checks if the letter guessed is in the game word: returns true or false
        """
        if self.letter_guess in list(self.game_word) and self.letter_guess in Game.alphabet:
            return True
        else:
            return False

    def change_hidden_letter(self):
        """
        Makes the guessed letter appear in the hidden game word
        """
        list_index = 0
        hidden_word_list = list(self.hidden_game_word)

        for letter in self.game_word:

            if letter == self.letter_guess:
                hidden_word_list[list_index] = self.letter_guess

            list_index += 1

        self.hidden_game_word = ''.join(hidden_word_list)
        return self.hidden_game_word

    def remove_letter_guess(self):
        """
        Removes the guessed letter from the  alphabet
        so it can not be guessed again
        """
        Game.alphabet.remove(self.letter_guess)
        return Game.alphabet

    def remove_life(self):
        """
        Removes life if an incorrect guess has been made
        """
        self.lives -= 1
        return self.lives


def reset_game():
    """
    Requests if player wants to reset another game or quit
    """
    reset = input("Would you like to play again (y/n): ")
    print("")

    if reset == "y":
        Game.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        main()
    else:
        print("Thank you for playing Hangman. We hope you had fun!!! Come back soon.")


def play_game(game_word, hidden_game_word, lives):
    """
    Main game play
    Checks whether game won, lost or to continue
    """
    game = Game("", game_word, hidden_game_word, lives)
    print(game.hidden_game_word)
    print("")

    print(game.alphabet)
    print("")

    letter_guess = input("Select a letter from the remaining in the letters above: ")
    print("")
    game.letter_guess = letter_guess

    if game.check_game_word():
        game.change_hidden_letter()
        game.remove_letter_guess()

        if game.hidden_game_word == game.game_word:
            print(f"Congratulations!!! You have guessed the correct answer which was {game.game_word}, with {game.lives} lives remaining.\n")
            reset_game()
        else:
            os.system('cls||clear')
            play_game(game.game_word, game.hidden_game_word, game.lives)

    else:
        game.remove_life()
        game.remove_letter_guess()

        if game.lives > 0:
            os.system('cls||clear')
            print(f"The letter '{game.letter_guess}' was not in the answer. You have {game.lives} lives remaining.\n")
            play_game(game.game_word, game.hidden_game_word, game.lives)
        else:
            os.system('cls||clear')
            print(game.hidden_game_word)
            print("")
            print(f"The letter {game.letter_guess} was not in the answer. You have 0 lives remaining. The answer which you was trying to guess was {game.game_word}.\n")
            reset_game()


def main():
    """
    Run all program functions
    """
    lives = select_difficluty()
    column = select_category()
    game_word = retrieve_word(column)
    hidden_game_word = hide_game_word(game_word)
    play_game(game_word, hidden_game_word, lives)


main()

