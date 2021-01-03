import pyglet

class ImageObject():
	def __init__(self, image, *args, **kwargs):
		if not 'batch' in kwargs: kwargs['batch'] = pyglet.graphics.Batch()
		if not 'debug' in kwargs: kwargs['debug'] = False
		self.updated = False
		self.debug = kwargs['debug']

		if not image and 'height' in kwargs and 'width' in kwargs and ('_noBackdrop' not in kwargs or kwargs['_noBackdrop'] == False):
			if self.debug:
				print(self, 'Generating image', kwargs)
			self.texture = self.generate_image(*args, **kwargs)
			#self._texture = self.texture.get_texture()
		elif type(image) == str:
			if self.debug:
				print(self, 'Loading file')
			self.texture = pyglet.image.load(image)
			#self._texture = self.texture.get_texture()
		elif type(image) == io.BytesIO:
			if self.debug:
				print(self, 'Loading bytes stream io.bytes')
			self.texture = pyglet.image.load(basename(kwargs['path']), file=image)
			#self._texture = self.texture.get_texture()
		elif type(image) == bytes:
			if self.debug:
				print(self, 'Loading bytes stream from bytes')
			tmp = io.BytesIO(image)
			self.texture = pyglet.image.load(basename(kwargs['path']), file=tmp)
		elif type(image) == ImageObject:
			if self.debug:
				print(self, 'Merging ImageObject')
			self.texture = image.texture
		else:
			if self.debug:
				print(self, 'Dummy ImageObject')

			self._x = kwargs['x']
			self._y = kwargs['y']
			self.texture = dummyTexture(*args, **kwargs)
			self._texture = self.texture.get_texture()
			self.batch = kwargs['batch']


	def generate_image(self, *args, **kwargs):
		if not 'width' in kwargs or not 'height' in kwargs:
			raise RenderError("Can not create image texture without width and height.")
		if not 'alpha' in kwargs: kwargs['alpha'] = 255
		if not 'color' in kwargs: kwargs['color'] = gfx.colors[choice(list(gfx.colors.keys()))]
		if 'debug' in kwargs and kwargs['debug']:
			print(f'{self}: generate_image({kwargs})')
		
		c = gfx.hex_to_colorpair(kwargs['color'])
		
		return pyglet.image.SolidColorImagePattern((*c, kwargs['alpha'])).create_image(kwargs['width'], kwargs['height'])

	def pixel(self, x, y, new_pixel):
		if self.texture:
			width = self.texture.width
			data = self.texture.get_image_data().get_data('RGBA', width*4)

			start = (width*4*y) + (x*4)
			data = data[:start] + new_pixel + data[start+4:]

			self.texture.set_data('RGBA', width*4, data)
			self.image = self.texture
		else:
			raise RenderError("Can not manipulate pixels on a empty ImageObject (initialize with width, height or texture first).")

	def update(self):
		pass

	def pre_render(self):
		pass

	def render(self):
		raise RenderError("Image object can't be drawn directly, wrap it in genericSprite()")