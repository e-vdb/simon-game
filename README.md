# SIMON-game with graphics user interface

## Summary
SIMON-game for one player.
Code written in python3 with graphics user interface (GUI) using Tkinter.

## SIMON-game
SIMON is a game to test your memory skills.

To learn more about SIMON : https://en.wikipedia.org/wiki/Simon_(game)

## Repository content
To play the game : save the following files in the same directory.
* simon.py : Python 3 script
* rules_eng.txt : plain text document that contains the rules of the game
* about.txt : plain text document that contains copyright and license information
* highScore.txt: plain text document used to record the high score
* highScore.gif : image taken from https://www.pngwing.com/en/free-png-shfbd


## Tkinter interface

![simonGUI](https://user-images.githubusercontent.com/82372483/131795649-611790ea-20a9-4990-8ad7-c75b5cdebedc.png)

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

![simonGUI_highScore](https://user-images.githubusercontent.com/82372483/131795766-fc349ec6-3f6a-44a8-a32f-26b017f6938e.png)


### Help

From the GUI you can read *How to play?* as well as copyright and license information.
