import gspread
from google.oauth2.service_account import Credentials
from random import randrange

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

    print("")
    print(f"You have selected game difficulty {difficulty} and will have {lives} lives.\n")

    return lives


def select_category():
    """
    Request for user to select the game category or for a random category to be chosen
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
        print("")
        print(f"You chose to guess something related to {categories_row[category_column]}.\n")
    else:
        category_column = randrange((len(categories_row)))
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
    game_word.upper()

    return game_word


def main():
    """
    Run all program functions
    """
    # lives = select_difficluty()
    column = select_category()
    game_word = retrieve_word(column)

main()
