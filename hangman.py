from datetime import date

today = date.today()
date = today.strftime("%d/%m/%Y")


def display_hangman(difficulty, lives):
    """
    Complete
    """
    if difficulty == "Easy":
        if lives == 0:
            hangman = f"""\
_________
|/       |
|        0
|       /|\\
|        |
|       / \\  ~ R.I.P ~
|___________ ~ {date} ~
            """
        elif lives == 1:
            hangman = """\
_________
|/       |
|        0
|       /|\\
|        |
|
|___________

1 Lives Remaining
            """
        elif lives == 2:
            hangman = """\
_________
|/       |
|        0
|        |
|        |
|
|___________

2 Lives Remaining
        """
        elif lives == 3:
            hangman = """\
_________
|/       |
|        0
|
|
|
|___________

3 Lives Remaining
        """
        elif lives == 4:
            hangman = """\
_________
|/       |
|
|
|
|
|___________

4 Lives Remaining
        """
        elif lives == 5:
            hangman = """\
_________
|/
|
|
|
|
|___________

5 Lives Remaining
        """
        elif lives == 6:
            hangman = """\

|/
|
|
|
|
|___________

6 Lives Remaining
        """
        else:
            hangman = " "
    elif difficulty == "Medium":
        if lives == 0:
            hangman = f"""\
_________
|/       |
|        0
|       /|\\
|        |
|       / \\  ~ R.I.P ~
|___________ ~ {date} ~
        """
        elif lives == 1:
            hangman = """\
_________
|/       |
|        0
|        |
|        |
|
|___________

1 Lives Remaining
        """
        elif lives == 2:
            hangman = """\
_________
|/       |
|        0
|
|
|
|___________

2 Lives Remaining
        """
        elif lives == 3:
            hangman = """\
_________
|/       |
|
|
|
|
|___________

3 Lives Remaining
        """
        elif lives == 4:
            hangman = """\
_________
|/
|
|
|
|
|___________

4 Lives Remaining
        """
        elif lives == 5:
            hangman = """\

|/
|
|
|
|
|___________

5 Lives Remaining
        """
        else:
            hangman = " "
    elif difficulty == "Hard":
        if lives == 0:
            hangman = f"""\
_________
|/       |
|        0
|       /|\\
|        |
|       / \\  ~ R.I.P ~
|___________ ~ {date} ~
        """
        elif lives == 1:
            hangman = """\
_________
|/       |
|        0
|        |
|        |
|
|___________

1 Life Remaining
        """
        elif lives == 2:
            hangman = """\
_________
|/       |
|        0
|
|
|
|___________

2 Lives Remaining
        """
        elif lives == 3:
            hangman = """\
_________
|/       |
|
|
|
|
|___________

3 Lives Remaining
        """
        elif lives == 4:
            hangman = """\

|/
|
|
|
|
|___________

4 Lives Remaining
        """
        else:
            hangman = " "

    return hangman
