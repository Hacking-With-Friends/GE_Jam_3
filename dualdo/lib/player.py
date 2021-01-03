import os
import pyglet
from .sprites import GeneralPurposeSprite

class Player(GeneralPurposeSprite):
	def __init__(self, view):
		self.view = view

		self.main_image = pyglet.image.load(f'{os.getcwd()}/resources/player.png')
		self.main_sprite = pyglet.sprite.Sprite(self.main_image, x=0, y=0)

	def render(self):
		# TODO: Ugly hack, shakes the carracter a bit, but /shrug :)
		real_x = 0+self.view.main_window.camera.x
		real_y = 0+self.view.main_window.camera.y

		self.main_sprite.x = real_x + self.view.main_window.width/2 - self.main_image.width/2
		self.main_sprite.y = real_y + self.view.main_window.height/2 - 20

		self.main_sprite.draw() # TODO: Set in batch instead :)