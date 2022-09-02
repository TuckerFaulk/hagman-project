from datetime import date

today = date.today()
date = today.strftime("%d/%m/%Y")


def display_hangman(difficulty, lives):
    """
    Complete
    """
    if difficulty == "Easy":
        if lives == 0:
            hangman = f"""
_________
|/       |
|        0
|       /|\\
|        |
|       / \\
|___________
~ R.I.P ~
~ {date} ~
            """
        elif lives == 1:
            hangman = """
_________
|/       |
|        0
|       /|\\
|        |
|
|___________
            """
        elif lives == 2:
            hangman = """
_________
|/       |
|        0
|        |
|        |
|
|___________
        """
        elif lives == 3:
            hangman = """
_________
|/       |
|        0
|
|
|
|___________
        """
        elif lives == 4:
            hangman = """
_________
|/       |
|
|
|
|
|___________
        """
        elif lives == 5:
            hangman = """
_________
|/
|
|
|
|
|___________
        """
        elif lives == 6:
            hangman = """

|/
|
|
|
|
|___________
        """
        else:
            hangman = " "
    elif difficulty == "Medium":
        if lives == 0:
            hangman = f"""
_________
|/       |
|        0
|       /|\\
|        |
|       / \\
|___________
~ R.I.P ~
~ {date} ~
        """
        elif lives == 1:
            hangman = """
_________
|/       |
|        0
|        |
|        |
|
|___________
        """
        elif lives == 2:
            hangman = """
_________
|/       |
|        0
|
|
|
|___________
        """
        elif lives == 3:
            hangman = """
_________
|/       |
|
|
|
|
|___________
        """
        elif lives == 4:
            hangman = """
_________
|/
|
|
|
|
|___________
        """
        elif lives == 5:
            hangman = """

|/
|
|
|
|
|___________
        """
        else:
            hangman = " "
    elif difficulty == "Hard":
        if lives == 0:
            hangman = f"""
_________
|/       |
|        0
|       /|\\
|        |
|       / \\
|___________
~ R.I.P ~
~ {date} ~
        """
        elif lives == 1:
            hangman = """
_________
|/       |
|        0
|        |
|        |
|
|___________
        """
        elif lives == 2:
            hangman = """
_________
|/       |
|        0
|
|
|
|___________
        """
        elif lives == 3:
            hangman = """
_________
|/       |
|
|
|
|
|___________
        """
        elif lives == 4:
            hangman = """

    |/
    |
    |
    |
    |
    |___________
        """
        else:
            hangman = " "

    return hangman

