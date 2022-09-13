# Hangman | Python Terminal Game! 

My idea for this project was to develop an online game for players to enjoy.

The object of the game is to:

- Suggest letters to see if they are contained in the hidden answer.
- If the letter is not in the hidden answer, you lose a life.
- To win the game, continue to suggest letters until all of the letters in the hidden answer are revealed.
- Although, if you guess too many incorrect letters and lose all your lives, the game is lost.

![Am I Responsive Image]()

The live link for the site can be found here - https://hangman-project-tf.herokuapp.com/

# Table of contents
- [Design](#design)
  - [Text and Background Color](#text-and-background-color)
  - [Game Area Design](#game-area-design)
  - [Game Process Planning Flow Chart](#game-process-planning-flow-chart)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Languages Used](#languages-used)
    - [Header including Navigation](#Header-including-navigation)
    - [Game Area](#game-area)
    - [Pop-up Messages](#pop-up-messages)
    - [How to Play](#how-to-play)
    - [Footer](#footer)
    - [Other Features](#other-features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Libraries and Programs Used](#libraries-and-programs-used)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

# Design

**Text and Background Color**



**Game Area Design**



**Game Process Planning Flow Chart**

![Flow Chart Process Plan]()

# Features

## Existing Features:

### Languages Used

- Python

### Logo and Subtitle



### How to Play


### Select Difficulty

### Select Category

### Main Game Area

- Category
- Hidden Word
- List of Remaining Letters
- Input Request

- Game Progress Message
- Hangman Design and Number of Lives Remaining
- Error Messages
- Game Won/Game Lost Message

- Request to reset the Game

### Validation Messages
#### - Alert Messages

![Alert Message 1]()
![Alert Message 2]()

## Other Features:

### Guess Answer

At any point, if the player thinks they know the answer, they can type there guess instead of a letter to see if they are correct and win the game.

- But note that if you guess incorrectly, a life will be lost.

### Adding Game Categories and Answers

I wanted to make sure that the answers and categories of the game were easy to add to. This was to keep the game interesting if players have guessed all of the possible answers in each category.

To do this, instead of having a list of answers as a variable, I set up an Excel Spreadsheet with columns of answers based on a category, and an API is used to retreive this information and randomise an answer.

Another bonus to this is that it makes the Hangman game customisable. Add answers of your favourite category or add keyword for something which you are revising.

The game has been programmed so, when a new Categorey is added, this is included as an option to be selected in the Category Section of the game. This category may also be selected when a 'Random' option is selected.

<!-- Show Image of the Category Section -->
<!-- Show image of a new Category in Excel -->
<!-- Show image of New Category Section -->

To add another Category and/or Answers:

Add New Category

1. Type in your new Category in the first row of the next empty column. 

2. Add your new answers in the column under the Category (NB: Ensure that the answers are typed in all lowercase). 

3. Save this file and your new category will be added as an option in the Hangman Game. The new answers added will then be selected randomly.

Add New Answers in an Existing Category

1. Just add new answers to the bottom of the list in the appropriate category and they will then be available to be randomly selected in the Hangman Game.

## Future Features

- Add a scoring system
- Add a high score table

# Testing



| Test   |      Expected      |  Passed |
|--------|:------------------:|--------:|
|        |                    | ☑      |
|        |                    | ☑      |
|        |                    | ☑      |


# Data Model


## Validator Testing

- PEP8Online:  

![PEP8Online Checker]()

- Lighthouse (Accessibility Audit): The page achieved a great accessibility performance.

![Lighthouse Accessibility Audit]()

## Unfixed Bugs

There were no unfixed bugs identified during the testing of this site.

## Libraries and Programs Used

- Github: Store Repository
- Gitpod: Create the html and css files
- Google Chrome, Microsoft Edge, Mozilla Firefox, Safari: Site testing on alternative browsers
- Microsoft OneNote: Planning notes for the project
- Am I Responsive: Screenshots of the final project for the README file

# Deployment

 

The live link for the site can be found here - https://hangman-project-tf.herokuapp.com/

# Credits



## Content



## Media

