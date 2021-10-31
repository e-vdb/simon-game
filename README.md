# SIMON-game with graphics user interface

## Summary
SIMON-game for one player.
Code written in python3 with graphics user interface (GUI) using Tkinter.

## SIMON-game
SIMON is a game to test your memory skills.

To learn more about SIMON : https://en.wikipedia.org/wiki/Simon_(game)

## simon folder content
To play the game : save all files from simon folder files into the same directory.
* main.py : main Python 3 script
* help_simon.py : Python 3 module
* stat_simon.py : Python 3 module
* rules_eng.txt : plain text document that contains the rules of the game
* about.txt : plain text document that contains copyright and license information
* highScore.txt: plain text document used to record the high score
* highScore.gif : image taken from https://www.pngwing.com/en/free-png-shfbd

## Tasks list
- [x] Implement python script
- [x] Add high score functionality
- [x] Add functionality in order to reset the current high score
- [ ] Document code

## Tkinter interface

![simon_game](https://user-images.githubusercontent.com/82372483/139250124-6841dfe4-9404-4e16-9de8-adedc535ea9f.png)


### Interface

* Four colored buttons
* One button *Play* to launch the sequence

### Gameplay

* Click on play to launch the sequence (the first one has a length of 1).
* The sequence is played. It highlights the buttons.
* Reproduce the sequence.
  * If you success, the sequence length is increased of 1.
  * If you fail, the game stops.
  * If your score is higher than the current high score, a window will open to ask you to enter your name.

### High score
The current high score is saved in a text document (player name and score). It can be displayed from the menu *Scores*.

![simon_game_high_score](https://user-images.githubusercontent.com/82372483/139250158-dc012c35-b151-44b2-a366-fd8471fe03d0.png)

### Help

From the GUI you can read *How to play?* as well as copyright and license information.
