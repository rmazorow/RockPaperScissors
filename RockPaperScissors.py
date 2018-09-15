"""
File: RockPaperScissors.py
Author: Rocky Mazorow

Plays the game of rock paper scissors with the user.
"""

from tkinter import *
import tkinter.messagebox
import random

class RockPaperScissors(Frame):

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
		
		#self._newGame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
		
	def _newGame(self):
		self._new.destroy()
		self._imageLabel.destroy()
		
		self._player = Label(self, text = "Player")
		self._player.grid(row = 0, column = 0)
		
		
		rImage = PhotoImage(file = "images/rock.gif")
		#self._rock = Button(self, image = rImage, width = 50, height = 50, command = lambda: self._play(1))
		self._rock = Button(self, text = "Rock", width = 10, command = lambda: self._play(1))
		#self._rock.configure(image = rImage, width = 100, height = 100)
		#self._rock.pack()
		self._rock.grid(row = 1, column = 0)
		
		self._paper = Button(self, text = "Paper", width = 10, command = lambda: self._play(2))
		'''pImage = PhotoImage(file = "images/paper.gif")
		self._paper.config(image = pImage, width = "100", height = "100")
		self._paper.pack()'''
		self._paper.grid(row = 2, column = 0)
		
		self._scissors = Button(self, text = "Scissors", width = 10, command = lambda: self._play(3))
		self._scissors.grid(row = 3, column = 0)
		
		self._message = StringVar()
		self._display = Label(self, textvariable = self._message, width = 10)
		self._display.grid(row = 1, column = 1)
		
		self._comp = Label(self, text = "Computer")
		self._comp.grid(row = 0, column = 2)
		
		self._imageLabel = Label(self, text = "")
		self._imageLabel.grid(row = 2, column = 2)
		
	def _play(self, player):
		comp = random.randint(1, 3)
		self._showComp(comp)
		
		self._rock.configure(state = DISABLED)
		self._paper.configure(state = DISABLED)
		self._scissors.configure(state = DISABLED)
		
		# rock = 1, paper = 2, scissors = 3
		if comp == player:
			self._message.set("You tie!")
		elif comp == 1 and player == 2:
			self._message.set("You win!")
		elif comp == 2 and player == 3:
			self._message.set("You win!")
		elif comp == 3 and player == 1:
			self._message.set("You win!")
		else:
			self._message.set("You lose!")	
		
		self._new = Button(self, text = "New Game", command = self._newGame)
		self._new.grid(row = 2, column = 1)		
		
	def _showComp(self, comp):
		if comp == 1:
			self._image = PhotoImage(file = "images/rock.gif")
		elif comp == 2:
			self._image = PhotoImage(file = "images/paper.gif")
		elif comp == 3:
			self._image = PhotoImage(file = "images/scissors.gif")
		self._imageLabel["image"] = self._image
		
		
def main():
	RockPaperScissors().mainloop()

main()