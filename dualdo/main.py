import time
import pyglet
from pyglet.gl import *
from lib.world import camera
from lib.scenes import mainMenu

class mainWindow(pyglet.window.Window):
	def __init__ (self, width=800, height=600, *args, **kwargs):
		super(mainWindow, self).__init__(width, height, *args, **kwargs)
		self.x, self.y = 0, 0

		self.camera = camera(self)
		self.view = mainMenu(self)

		self.log_array = []

		self.log_document = pyglet.text.document.FormattedDocument()
		self.log_document.text = '\n'.join(self.log_array)
		self.log_document.set_style(0, len(self.log_document.text), dict(font_name='Arial', font_size=12, color=(128, 128, 128,255)))
		
		self.log_layout = pyglet.text.layout.TextLayout(self.log_document, 240, 12*self.log_document.text.count('\n'), multiline=True, wrap_lines=False)
		self.log_layout.x=self.camera.x+10
		self.log_layout.y=self.camera.y+14*self.log_document.text.count('\n')
		self.log_layout.anchor_x='left'
		self.log_layout.anchor_y='bottom'
	
		self.keys = {}
		
		self.mouse_x = 0
		self.mouse_y = 0

		self.alive = 1

		glClearColor(0/255, 0/255, 0/255, 0/255)

	def log(self, *args):
		self.log_array.append(''.join(args))
		self.log_document.text = '\n'.join(self.log_array[-5:])
		self.log_document.set_style(0, len(self.log_document.text), dict(font_name='Arial', font_size=12, color=(128, 128, 128,255)))
		self.log_layout.height = 12*(self.log_document.text.count('\n')+1)
		self.log_layout.y=12*(self.log_document.text.count('\n')+1)

	def on_draw(self):
		self.render()

	def on_close(self):
		self.alive = 0

	def on_mouse_motion(self, x, y, dx, dy):
		self.mouse_x = x
		self.mouse_y = y

	def on_mouse_release(self, x, y, button, modifiers):
		self.log(f'Mouse released: {x,y}')
	
	def on_mouse_press(self, x, y, button, modifiers):
		self.log(f'Mouse pressed: {x,y}')

	def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
		self.drag = True

		if self.log_array[-1] != f'Mouse draging {self.view}':
			self.log(f'Mouse draging {self.view}')

	def on_key_release(self, symbol, modifiers):
		self.log(f'Key released: {pyglet.window.key.symbol_string(symbol)}')
		del(self.keys[symbol])

	def on_key_press(self, symbol, modifiers):
		if symbol == pyglet.window.key.ESCAPE: # [ESC]
			self.alive = 0

		self.keys[symbol] = time.time()

		self.log(f'Key pressed: {pyglet.window.key.symbol_string(symbol)}')

	def render(self):
		self.log_layout.x=self.camera.x+10
		self.log_layout.y=self.camera.y+14*self.log_document.text.count('\n')

		glClear( GL_COLOR_BUFFER_BIT )

		# Initialize Projection matrix
		glMatrixMode( GL_PROJECTION )
		glLoadIdentity()

		# Initialize Modelview matrix
		glMatrixMode( GL_MODELVIEW )
		glLoadIdentity()

		# Set orthographic projection matrix
		glOrtho(*self.camera, 1, -1 )

		if pyglet.window.key.W in self.keys:
			self.camera.move('UP')
		if pyglet.window.key.A in self.keys:
			self.camera.move('LEFT')
		if pyglet.window.key.S in self.keys:
			self.camera.move('DOWN')
		if pyglet.window.key.D in self.keys:
			self.camera.move('RIGHT')

		self.view.render()

		if self.log_array:
			self.log_layout.draw()

		self.flip()

	def run(self):
		while self.alive == 1:
			self.render()

			# -----------> This is key <----------
			# This is what replaces pyglet.app.run()
			# but is required for the GUI to not freeze
			#
			event = self.dispatch_events()

if __name__ == '__main__':
	x = mainWindow()
	x.run()