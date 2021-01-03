import pyglet
from .images import ImageObject

class GeneralPurposeSprite(ImageObject, pyglet.sprite.Sprite):
	def __init__(self, texture=None, parent=None, moveable=True, *args, **kwargs):
		if not 'x' in kwargs: kwargs['x'] = 0
		if not 'y' in kwargs: kwargs['y'] = 0
		if not 'debug' in kwargs: kwargs['debug'] = False
		if not 'batch' in kwargs: kwargs['batch'] = pyglet.graphics.Batch()
		if not 'dragable' in kwargs: kwargs['dragable'] = False
		self.debug = kwargs['debug']

		ImageObject.__init__(self, texture, *args, **kwargs)

		#self.batch = kwargs['batch']
		self.sprites = {}

		if self.texture:
			sprite_kwargs = kwargs.copy()
			for item in list(sprite_kwargs.keys()):
				# List taken from: https://pyglet.readthedocs.io/en/stable/modules/sprite.html#pyglet.sprite.Sprite
				if item not in ('img', 'x', 'y', 'blend_src', 'blend_dest', 'batch', 'group', 'usage', 'subpixel'):
					del(sprite_kwargs[item])
			if self.debug:
				print(f'{self}: Creating a Sprite({sprite_kwargs})')
			pyglet.sprite.Sprite.__init__(self, self.texture, **sprite_kwargs)
			if 'width' in kwargs: self.resize(width=kwargs['width'])
			if 'height' in kwargs: self.resize(height=kwargs['height'])
		else:
			if self.debug:
				print(f'{self}: Creating a dummy Sprite({kwargs})')
			self.draw = self.dummy_draw
			self._x = kwargs['x']
			self._y = kwargs['y']
			self._texture = dummyTexture(kwargs['width'], kwargs['height'], *args, **kwargs)
			print(self, self._texture)
			#moo = pyglet.sprite.Sprite(self.generate_image(*args, **kwargs))
			self.batch = kwargs['batch']
			#self.render = self.dummy_draw
			#self.x = kwargs['x']
			#self.y = kwargs['y']

		self._rot = 0
		self.dragable = kwargs['dragable']

	def resize(self, width=None, height=None, *args, **kwargs):
		if width:
			self._texture.width = width
		if height:
			self._texture.height = height

	def update(self, *args, **kwargs):
		pass

	def pre_render(self, *args, **kwargs):
		pass

	def dummy_draw(self):
		pass

	def rotate(self, deg, adjust_anchor=True):
		anchors = self._texture.anchor_x, self._texture.anchor_y
		if(anchors == (0, 0) and adjust_anchor):
			x,y = self.x, self.y
			self.x = x + (self.width/2)
			self.y = y + (self.height/2)

		if adjust_anchor:
			self._texture.anchor_x = self.width / 2
			self._texture.anchor_y = self.height / 2

		self._rot = (self._rot + deg) % 360
		self.rotation = self._rot

		#self._texture.anchor_x, self._texture.anchor_y = anchors
		

	def move(self, dx, dy):
		if self.dragable:
			self.x += dx
			self.y += dy
			for sprite in self.sprites:
				self.sprites[sprite].x += dx
				self.sprites[sprite].y += dy

	def hover(self, x, y):
		pass

	def hover_out(self, x, y):
		pass

	def click(self, x, y, button=None):
		pass

	def mouse_down(self, x, y, button=None):
		pass

	def mouse_up(self, x, y, button=None):
		pass

	def mouse_inside(self, x, y, mouse_button=None):
		if self.debug:
			print(f'Inside: {self}, {x, y} | {self.x,self.y}, {self.width, self.height}')
			print(f' {x >= self.x} and {y >= self.y}')
			print(f'   {x <= self.x+self.width} and {y <= self.y+self.height}')
		if x >= self.x and y >= self.y:
			if x <= self.x+self.width and y <= self.y+self.height:
				if self.debug:
					print('   yes')
				return self

	def render(self):
		self.batch.draw()
#		self.draw()