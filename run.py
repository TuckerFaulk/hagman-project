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


def select_category():
    """
    Request for user to select word category or for a random category to be chosen
    """
    print("Please select one of the following categories, or choose 'Random' if you would like us to pick one for you.\n")

    categories = SHEET.worksheet("categories")
    data = categories.get_all_values()
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
        print(f"")
        print(f"The random category selected for you is {categories_row[category_column]}.\n")
    
    return category_column
