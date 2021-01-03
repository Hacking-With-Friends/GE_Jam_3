class camera():
	def __init__(self, main_window, x=0, y=0, scale=1.0):
		self.x = x
		self.y = y
		self.scale = scale
		self.main_window = main_window

	def __iter__(self):
		return iter([self.x, self.x+self.main_window.width, self.y, self.y+self.main_window.height])

	def __repr__(self):
		return f"<Camera @ x: {self.x}, y: {self.y} (scale: {self.scale})>"

	def move(self, direction):
		if direction == 'UP':
			self.y += 1
		elif direction == 'DOWN':
			self.y -= 1
		elif direction == 'LEFT':
			self.x -= 1
		elif direction == 'RIGHT':
			self.x += 1