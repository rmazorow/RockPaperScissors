# RockPaperScissors

## Synopsis
Plays the game of rock paper scissors with the user

## Motivation
This is a demonstration of a tkinter GUI in Python 3. This was created for an application for an instructor position at a girls' summer coding camp.

## How to Play
Download game and run .py file. 

## Code Example
This code snippet is the constructor for the game.
```
def __init__(self):
		"""Set up the window and widgets."""
		Frame.__init__(self)
		self.master.title("Rock Paper Scissors")
		self.master.geometry("350x200")
		self.master.resizable(0, 0)
		self.grid()
		
		self._new = Button(self, text = "New Game", command = self._newGame)
		self._new.grid(row = 1, column = 2)
		
		self._imageLabel = Label(self, text = "")
		self._imageLabel.grid(row = 2, column = 2)
```
