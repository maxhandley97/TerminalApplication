# Max Handley's Terminal application
# Installation instructions are at the bottom of the document
 ## Links to referenced sources
[PEP 8 Style Guide](https://peps.python.org/pep-0008/)  
[Colorama](https://pypi.org/project/colorama/)  
[Termcolor](https://pypi.org/project/termcolor/)  
All other imports are built in with Python
 ## R4 [Source control repo](https://github.com/maxhandley97/TerminalApplication)
 ## Code style guide - PEP 8
I've adhered to conventions used in PEP 8 to create clearly readable code:
- Methods/Classes are logically named
- Indentation was used relevantly, with 4 spaces. 
- Maximum length of code doesn't surpass 79 characters.  
- Imports are logically listed
- Whitespaces are minimised
## Features in Terminal application
**Gameboard**  
This Feature handles simple processes related to the gameboard, used in all game modes. This is encapsulated by the following methods: 
- the printing of the board 
- restarting the board between games 
- checking user/bot inputs, whether board placements are valid 
- the placement of markers and therefore updating printed board in terminal
- Defining player win and tie games

**Game controller - PVP**  
This feature handles the bulk of the program's processes. All user inputs, menus and main controls are handled here, methods involved are detailed below:
- Turn on game defines what the user sees when the game is started
- The main menu which allows user to select game mode
- Handles errors if user input is incorrect in menu selection
- Handles messages within gameplay, prompting users to correctly place markers and options for when game is completed 
- Creates a score tally used in all game modes, to print and keep current score of games
- Handles player alternation, so advantages aren't given between multiple rounds of play

**Game controller - PVE**  
I attempted to create a seperate file and module for player vs bot, to avoid creating a god class. I kept running into cicular import issues and found it difficult without wetting my code immensely. I also did research into creating an unbeatible bot, but in my attempts I didn't want to push broken code and ran out of time. Methods used within the PVE:
- Dry game code, being usable in all game modes
- Randomised bot marker placement when in Player vs Bot mode
- Bot specific chatter to create atmosphere when versing bot


**Main**  
This feature imports game controller and starts application

## Implementation Plan
### Board implementation process
- [x] Create array for markers
- [x] Print board method
- [x] Add logic to display board in terminal
- [x] Determine state to track and validate correct marker placements
- [x] Determine whether box is empty

## Main Menu implementation process
- [x] Allow player 1 to enter name
- [x] Create functional menu
- [x] Add font to menu
- [x] Account for input errors

## Player vs Player
- [x] Allow player 2 to enter name and allocate associated marker
- [x] Accept input from player(s)
- [x] Keep track of player moves
- [x] Demarcate player 1 in color for distinguishing moves
- [x] Keep track of score by player name

## Player vs Bot
- [x] Assign game type title
- [x] Replace player 2 with bot for DRY code
- [x] Add bot logic for how bot plays
- [x] Assign gamescore to PVE keep track
- [x] Add functionality to bot to distinguish and create animated environment

## Screenshots
![Screenshot1](/docs/images/Screenshot12023-10-21.jpeg)
![Screenshot2](/docs/images/Screenshot22023-10-21.jpeg)
![Screenshot3](/docs/images/Screenshot32023-10-22.png)
![Screenshot4](/docs/images/Screenshot42023-10-24.png)
![Screenshot5](/docs/images/Screenshottesting2023-10-26.png)
![Screenshot6](/docs/images/ScreenshotDone2023-10-27.png)

## Installation Instructions
Python3 is a requirement:
**To install game**  
Type the following into two commands seperately in terminal:
1. ./scripts/install.sh  
2. ./scripts/start_game.sh
