import os
import pyglet
from .sprites import GeneralPurposeSprite

class Platform(GeneralPurposeSprite):
	def __init__(self, view):
		self.view = view

		self.main_image = pyglet.image.load(f'{os.getcwd()}/resources/platform.png')
		self.main_sprite = pyglet.sprite.Sprite(self.main_image, x=0, y=0)

	def render(self):
		self.main_sprite.draw() # TODO: Set in batch instead :)