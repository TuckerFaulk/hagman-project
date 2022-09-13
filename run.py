from random import randrange # generates random numbers
import os
from time import sleep  # allows time delay for print statements
from pyfiglet import Figlet
from termcolor import colored
import gspread
from google.oauth2.service_account import Credentials
from hangman import display_hangman


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


def game_title():
    """
    Clears the console and displays the game title
    """
    os.system('cls||clear')
    f = Figlet(font='big')
    title = f.renderText("HANGMAN")
    title += "Created by Thomas Faulkner | Code Institute Python Project\n"
    colored_title = colored(title, on_color="on_blue")
    print(colored_title)


def how_to_play():
    """
    Displays the rules of the game
    """
    sleep(2)
    print("Guess the mystery answer one letter at a time before you run out of lives.\n")
    sleep(2)
    print("If you are feeling lucky, type a guess instead of a letter to see if you are correct.\n")
    sleep(2)


def select_difficluty():
    """
    Request for user to select game difficulty: Hard (5 Lives),
    Medium (6 Lives), Easy (7 Lives)
    """
    # os.system('cls||clear')
    while True:
        print("Please select your game difficulty.\n")

        game_difficulty = {"Hard": 5, "Medium": 6, "Easy": 7}

        num = 1

        for difficulty, lives in game_difficulty.items():
            print(f"{num} - {difficulty} ({lives} Lives)")
            num += 1

        print("")
        input_value = input("Which difficulty would you like to select (1-3)?\n")

        if validate_data(input_value, 3):
            break

    input_value = int(input_value)

    input_value -= 1

    difficulty = list(game_difficulty)[input_value]
    lives = list(game_difficulty.values())[input_value]

    os.system('cls||clear')
    print(f"You have selected game difficulty {difficulty} and will have {lives} lives.\n")

    return difficulty, lives


def select_category():
    """
    Request for user to select the game category or for a random category to
    be chosen
    """
    while True:
        print("Please select one of the following categories, or choose 'Random' if you would like us to pick one for you.\n")

        data = CATEGORIES.get_all_values()
        categories_row = data[0]

        num = 1

        for category in categories_row:
            print(f"{num} - {category}")
            num += 1

        print(f"{num} - Random\n")

        num_of_categories = len(categories_row) + 1

        category_input = input(f"Which category number would you like to select (1-{num_of_categories})?\n")

        if validate_data(category_input, num_of_categories):
            break

    category_input = int(category_input)

    category_column = category_input - 1

    if category_input <= len(categories_row):
        os.system('cls||clear')
        category = categories_row[category_column]
        print("You have chosen to guess something related to:\n")
    else:
        category_column = randrange((len(categories_row)))
        category = categories_row[category_column]
        os.system('cls||clear')
        print(f"The random category selected for you is: \n")

    category_column += 1

    return category_column, category


def validate_data(value, num_of_options):
    """
    Inside the try checks whether an interger has been entered and
    whether it is within the range of the number of options.
    Raises ValueError or IndexError as appropriate.
    """

    try:
        int(value)

        if int(value) > num_of_options:
            raise IndexError(
                f"Please enter a value between 1-{num_of_options}. You entered '{value}'"
            )

    except ValueError as e:
        os.system('cls||clear')
        error_message = colored(f"ValueError: Please enter a value between 1-{num_of_options}. You entered '{value}'.\n", on_color="on_red")
        print(error_message)
        return False

    except IndexError as e:
        os.system('cls||clear')
        error_message = colored(f"IndexError: {e}.\n", on_color="on_red")
        print(error_message)
        return False

    return True


def retrieve_word(column):
    """
    Retrieve word, phrase or sentence from the selected category column
    """
    column_values = CATEGORIES.col_values(column)
    column_values.pop(0)
    rand_column_cell = randrange((len(column_values)))
    game_word = column_values[rand_column_cell]

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
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self, letter_guess, game_word, hidden_game_word, lives, category):
        self.letter_guess = letter_guess
        self.game_word = game_word
        self.hidden_game_word = hidden_game_word
        self.lives = lives
        self.category = category

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
                hidden_word_list[list_index] = self.letter_guess.upper()

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
    Input 'y' starts the game again
    Any other input will close the game
    """
    reset = input("Would you like to play again (y/n)?:\n")

    if reset.lower() == "y":
        Game.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        main()
    else:
        game_title()
        print("Thank you for playing Hangman. We hope you had fun!!! Come back soon.\n")


def display_game_word(game_word):
    """
    Changes the "/" in the game word to spaces, and capitalizes each the first letter of each word
    """
    game_word = game_word.title()

    display_word = []

    for letter in game_word:
        if letter == "/":
            display_word.append(" ")
        else:
            display_word.append(letter)

    display_word = ''.join(display_word)

    return display_word


def game_won(game_word, lives, category, hidden_game_word, alphabet, hangman):
    """
    Displays Game Won message, then runs reset_game()
    """
    os.system('cls||clear')

    game_word = display_game_word(game_word)
    f = Figlet(font='big')
    title = f.renderText("CONGRATS!!!")
    colored_title = colored(title, on_color="on_blue")

    print(colored_title)
    print(f"You have guessed the correct answer which was {game_word}, with {lives} lives remaining.\n")

    reset_game()


def play_game(game_word, hidden_game_word, lives, category, difficulty):
    """
    Main game play
    Checks whether game won, lost or to continue
    """
    while True:
        game = Game("", game_word, hidden_game_word, lives, category)

        print(f"{game.category}\n")
        print(f"{game.hidden_game_word}")

        hangman = display_hangman(difficulty, game.lives)
        print(hangman)

        display_alphabet = ''.join(game.alphabet)
        print(f"Remaining letters: {display_alphabet.upper()}\n")

        letter_guess = input("Select a letter from the remaining in the letters above (or type your guess):\n")

        # Guess Game Word Feature: if a string more than 3 letters is input,
        # the following treats it as a guess and checks if it is equal to the game word.
        # Removes a life if the guess is incorrect

        if len(letter_guess) > 3:
            if letter_guess.title() == display_game_word(game.game_word):
                game_won(game.game_word, game.lives, game.category, game.hidden_game_word, game.alphabet, hangman)
                return None
            else:
                game.remove_life()

            if game.lives > 0:
                os.system('cls||clear')
                print(f"You guessed that the answer is '{letter_guess}' which is incorrect. You have {game.lives} lives remaining.\n")
                play_game(game.game_word, game.hidden_game_word, game.lives, game.category, difficulty)
            else:
                os.system('cls||clear')
                game_word = display_game_word(game.game_word)

                f = Figlet(font='big')
                title = f.renderText("UNLUCKY!!!")
                colored_title = colored(title, on_color="on_blue")

                print(colored_title)
                print(f"You guessed that the answer is '{letter_guess}' which is incorrect. You have 0 lives remaining. The answer which you was trying to guess was {game_word}.\n")

                print(f"{game.category}\n") # Update
                print(game.hidden_game_word)
                hangman = display_hangman(difficulty, game.lives)
                print(hangman)
                print(f"Remaining letters: {display_alphabet.upper()}\n")
                reset_game()

        elif validate_letter(letter_guess, game.alphabet):
            break

    game.letter_guess = letter_guess.lower()

    if game.check_game_word():
        game.change_hidden_letter()
        game.remove_letter_guess()

        if game.hidden_game_word.lower() == game.game_word:
            game_won(game.game_word, game.lives, game.category, game.hidden_game_word, game.alphabet, hangman)
        else:
            os.system('cls||clear')
            play_game(game.game_word, game.hidden_game_word, game.lives, game.category, difficulty)
    else:
        game.remove_life()
        game.remove_letter_guess()

        if game.lives > 0:
            os.system('cls||clear')
            print(f"The letter '{game.letter_guess}' is not in the answer. You have {game.lives} lives remaining.\n")
            play_game(game.game_word, game.hidden_game_word, game.lives, game.category, difficulty)
        else:
            os.system('cls||clear')

            game_word = display_game_word(game.game_word)

            f = Figlet(font='big')
            title = f.renderText("UNLUCKY!!!")
            colored_title = colored(title, on_color="on_blue")

            print(colored_title)
            print(f"The letter '{game.letter_guess}' is not in the answer. You have 0 lives remaining. The answer which you was trying to guess was {game_word}.")

            hangman = display_hangman(difficulty, game.lives)
            print(hangman)

            reset_game()


def validate_letter(letter_guess, remaining_letters):
    """
    Inside the try checks whether an string has been entered and
    whether it is within the list of remaining letters to guess.
    Raises ValueError as appropriate.
    """
    letter_guess = letter_guess.lower()
    try:
        str(letter_guess)

        if letter_guess not in remaining_letters:
            raise ValueError(
                f"You entered '{letter_guess}'"
            )

    except ValueError as e:
        os.system('cls||clear')
        error_message = colored(f"ValueError: {e}. Please enter one of the remaining letters (shown below).\n", on_color="on_red")
        print(error_message)
        return False

    return True


def main():
    """
    Run all program functions
    """
    game_title()
    how_to_play()
    difficulty, lives = select_difficluty()
    column, category = select_category()
    game_word = retrieve_word(column)
    hidden_game_word = hide_game_word(game_word)
    play_game(game_word, hidden_game_word, lives, category, difficulty)


main()

