import os
from pyglet.gl import *

from .player import Player
from .platform import Platform

class mainMenu():
	def __init__(self, main_window):
		self.main_window = main_window

		self.main_batch = pyglet.graphics.Batch()
		depressed = pyglet.image.load(f'{os.getcwd()}/resources/play_game_button.png')
		pressed = pyglet.image.load(f'{os.getcwd()}/resources/play_game_button.png')

		self.frame = pyglet.gui.Frame(self.main_window, order=4)
		self.play_button = pyglet.gui.ToggleButton(100, 400, pressed=pressed, depressed=depressed, batch=self.main_batch)
		self.play_button.set_handler('on_toggle', self.play_game)
		self.frame.add_widget(self.play_button)

	def play_game(self, value):
		self.main_window.view = GameView(self.main_window)

	def render(self):
		glClearColor(25/255, 94/255, 131/255, 0/255)
		self.main_batch.draw()

class GameView():
	def __init__(self, main_window):
		self.main_window = main_window

		self.platform = Platform(self)
		self.player = Player(self)

	def render(self):
		glClearColor(94/255, 25/255, 131/255, 0/255)
		self.platform.render()
		self.player.render()