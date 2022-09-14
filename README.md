# Hangman | Python Terminal Game! 

![Am I Responsive Image](assets/readme-images/am-i-responsive.jpg)

My idea for this project was to develop an online game for players to enjoy.

The object of the game is to:

- Suggest letters to see if they are contained in the hidden answer.
- If the letter is not in the hidden answer, you lose a life.
- To win the game, continue to suggest letters until all of the letters in the hidden answer are revealed.
- Although, if you guess too many incorrect letters and lose all your lives, the game is lost.

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

# Design and Planning

**Logo Font and Color**

I initially found it difficult to add 'design' to a terminal game and that this was mostly limited to formatting. From some research, I did find the 'pyfiglet' and 'termcolor' libraries which could be used to change text font and add color to text printed in the terminal.

My original design for my Logo was as below, but after some feedback during testing, it was reported that the font was difficult to read and as such, a font was chosen for a better user experience.

Original Logo

![Original Logo](assets/readme-images/original-logo-font.png)

New Logo

![Original Logo](assets/readme-images/new-logo-font.jpg)

Once the font and color was finalised, it was used for the game won and game lost messages. It was decided for the same color to be used for these messages as the title to keep with the theme of the game.

Game Won Message

![Game Won Message](assets/readme-images/game-won-message.jpg)

Game Lost Message

![Game Lost Message](assets/readme-images/game-lost-message.jpg)

**Error Messages**

The final bit of coloring added to the game was to highlight error messages in red. This was so they could be distinguished from the game text and to alert the player.

Sample Error Message - Highlighted Red

![Error Message](assets/readme-images/value-error-message.jpg)

**Game Process Planning Flow Chart**

With there being many steps in the code and different decision stages, I initially planned out the game by setting out in stage on a flow chart.

![Flow Chart Process Plan]()

# Languages Used

- Python

# Features

## Existing Features:

### Logo and Subtitle



### How to Play

I have added a 'How to Play?' section to ensure that the player understands the objective of the game and this section also introduces the feature for the player to guess the whole answer at any point in the game.

### Select Difficulty

To make the game more interesting for the player, I have added a difficulty level which they are able to select. Each difficulty level corresponds to a number of lives: Easy = 7 Lives; Medium = 6 Lives; Hard = 5 Lives.

### Select Category

An option has been added for the player to select a category for answer which they would like to guess. If they player is feeling lucky, they are able to select for a random category to be chosen.

### Main Game Area

- Display Category: Reminds the player of the category of the answer.
- Hidden Word: The word, phase or sentence which the player is trying to guess. This updates as letters are guessed correctly.
- List of Remaining Letters: Reminds the player of the list of letters which they have left to guess from.
- Input Request: Requests for the player to guess a letter or the answer.

- Game Progress Message
- Hangman Design and Number of Lives Remaining: Follows the classic design of the Hangman game as an incorrect guess is made.
- Error Messages
- Game Won/Game Lost Message

- Request to reset the Game

## Other Features:

### Guess Answer

At any point, if the player thinks they know the answer, they can type there guess instead of a letter to see if they are correct and win the game. If an incorrect guess is made, a life will be lost.

To ensure that there is room for error from the player, the game will only accept an answer guess if it is longer than 3 characters (the shortest answer to guess is 4 characters long). This means that if the player accidentially submits two or three random letters, this is not accepted and an error message is displayed.

### Adding Game Categories and Answers

I wanted to make sure that the answers and categories of the game were easy to add to. This was to keep the game interesting if players have guessed all of the possible answers in each category.

To do this, instead of having a list of answers as a variable, I set up an Excel Spreadsheet with columns of answers based on a category, and an API is used to retreive this information and randomise an answer.

Another bonus to this is that it makes the Hangman game customisable. Add answers of your favourite category or add keyword for something which you are revising.

The game has been programmed so, when a new Categorey is added, this is included as an option to be selected in the Category Section of the game. This category may also be selected when a 'Random' option is selected.

<!-- Show Image of the Category Section -->
<!-- Show image of a new Category in Excel -->
<!-- Show image of New Category Section -->

Link for the Category Spreadsheet: https://docs.google.com/spreadsheets/d/1yZvlt76H67GoI1nYCoELXNyLjRzGpB4CzKvvJ7s4E1k/edit#gid=0

To add another Category and/or Answers:

**Add New Category**

1. Type in your new Category in the first row of the next empty column. 

2. Add your new answers in the column under the Category (NB: Ensure that the answers are typed in all lowercase). 

3. Save this file and your new category will be added as an option in the Hangman Game. The new answers added will then be selected randomly.

**Add New Answers in an Existing Category**

1. Just add new answers to the bottom of the list in the appropriate category and they will then be available to be randomly selected in the Hangman Game.

## Future Features

- Add a scoring system
- Add a high score table

# Data Model

## Classes and Object Oriented Programming

I wanted to use a class for the main varibles of the game with methods for updating the game.

# Testing

| Test   |      Expected      |  Passed |
|--------|:------------------:|--------:|
|        |                    | ☑      |
|        |                    | ☑      |
|        |                    | ☑      |

# Debugging

I was having an issue with the Figlet title in the Heroku deployed version of the game where it started to stack when it should have been clearing the terminal.

- Checking throughout the code to see if the game_title function had been called more thano once.
- Student Support

Solution

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

This project was deployed on Heroku using Code Institute's Python Essentials template. The steps taken to create the Heroku App were:

**Preparing for deployment on GitHub:**

1. Add a new line character ("\n") after each input request
2. Type into the terminal 'pip3 freeze > requirements.txt' to update this file with a list of dependencies which Heroku needs to download for the application to work

**Deploying on Heroku:**

1. Create App
2. Add creds.json file information to the Apps Config Vars
3. Add the 'Python' and the 'Nodejs' buildpacks
4. Select the GitHub Delpoyment Method, and confirm the connection to GitHub
5. Search and connect to the Hangman Game GitHub Respository
6. Enable 'Automatic Deploys'
7. Then Maually deploy by selecting the 'Deploy Branch' button
8. The app will then be successfully deployed: press the 'view' button to open the deployed site 

The live link for the site can be found here - https://hangman-project-tf.herokuapp.com/

# Credits



## Content

Code Institute's Love Sandwiches Walkthrough Project:

- Getting Set Up (Creating the Google Sheets API)
- Deployment (Deployment to Heroku)
