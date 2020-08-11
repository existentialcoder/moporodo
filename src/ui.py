import tkinter as tk

class UI:
	"""Class containinng all UI related methods"""

	def __init__(self):
		"""
		creates root tk object, sets title, sets window size to full screen and binds tab key to allow toggling window size
		"""

		root = tk.Tk()
		root.title("Moporodo")
		self.showFullscreen = True
		root.attributes("-fullscreen", self.showFullscreen)
		root.bind("<Tab>", self.toggle_fullscreen)
		self.root = root

	def toggle_fullscreen(self, event=None):
		"""
		toggles fullscreen on and off based on the current value

		Parameters:
		event (object): details of event which triggered this function
		"""

		self.showFullscreen = not self.showFullscreen
		self.root.attributes("-fullscreen", self.showFullscreen)

	def add_label(self, root=None, **args):
		"""
		adds a label to the root

		Parameters:
		root (object): root tkinter object

		Keyword Parameters:
		text (string): label text
		bg (string): background color value
		fg (string): text/fg color value
		font (string): font for label text
		height (int): height of label
		width (int): width of label
		padx (int): horizontal padding
		pady (int): vertical padding

		Returns:
		object: tk label object
		"""

		if root is None:
			root = self.root
		label = tk.Label(root, args)
		label.pack()
		return label

	def add_button(self, root=None, **args):
		"""
		adds a button to the root

		Parameters:
		root (object): root tkinter object

		Keyword Parameters:
		text (string): button text
		command (function): function to be triggered when button is clicked
		image (string): path of image (to be displayed instead of text)
		bg (string): background color value
		fg (string): text/fg color value
		font (string): font for button text
		height (int): height of button
		width (int): width of button
		padx (int): horizontal padding
		pady (int): vertical padding
		state (int): state of the button (ACTIVE, NORMAL, DISABLED)

		Returns:
		object: tk button object
		"""

		if root is None:
			root = self.root
		button = tk.Button(root, args)
		button.pack()
		return button

	def add_canvas(self, root=None, **args):
		"""
		adds a canvas to the root

		Parameters:
		root (object): root tkinter object

		Keyword Parameters:
		bg (string): background color value
		height (int): height of canvas
		width (int): width of canvas

		Returns:
		object: tk canvas object
		"""

		if root is None:
			root = self.root
		canvas = tk.Canvas(root, args)
		canvas.pack()
		return canvas

	def add_frame(self, root=None, **args):
		"""
		adds a frame to the root

		Parameters:
		root (object): root tkinter object

		Keyword Parameters:
		bg (string): background color value
		height (int): height of frame
		width (int): width of frame

		Returns:
		object: tk frame object
		"""

		if root is None:
			root = self.root
		frame = tk.Frame(root, args)
		frame.pack()
		return frame

	def add_check_button(self, root=None, **args):
		"""
		adds a check button to the root

		Parameters:
		root (object): root tkinter object

		Keyword Parameters:
		text (string): check button text
		command (function): function to be triggered when check button is ticked
		image (string): path of image (to be displayed instead of text)
		bg (string): background color value
		fg (string): text/fg color value
		font (string): font for check button text
		height (int): height of check button
		width (int): width of check button
		padx (int): horizontal padding
		pady (int): vertical padding
		state (int): state of the check button (ACTIVE, NORMAL, DISABLED)
		selectcolor (string): color of check box when check button is selected

		Returns:
		object: tk check button object
		"""

		if root is None:
			root = self.root
		check_button = tk.Checkbutton(root, args)
		check_button.pack()
		return check_button

	def add_entry(self, root=None, **args):
		"""
		adds an input/entry to the root

		Parameters:
		root (object): root tkinter object

		Keyword Parameters:
		command (function): function to be triggered when check button is ticked
		bg (string): background color value
		fg (string): text/fg color value
		selectbackground (string): background color value of selected text
		selectforeground (string): foreground color value of selected text
		font (string): font for entry text
		width (int): width of entry
		show (string): set this to a character if you do not want the input to show the characters being typed (ex: when typing a password)

		Returns:
		object: tk entry object
		"""

		if root is None:
			root = self.root
		entry = tk.Entry(root, args)
		entry.pack()
		return entry

	def create_rectangle(self, root, x1, y1, x2, y2, **args):
		"""
		adds a rectangle to the root

		Parameters:
		root (object): root tkinter object
		x1 (int): x-coordinate of left corner of rectangle
		y1 (int): y-coordinate of left corner of rectangle
		x2 (int): x-coordinate of right corner of rectangle
		y2 (int): y-coordinate of right corner of rectangle

		Keyword parameters:
		fill (string): fill colour of rectangle

		Returns:
		object: tk canvas rectangle object
		"""

		rectangle = root.create_rectangle(x1, y1, x2, y2, args)
		return rectangle

	def render(self, root=None):
		"""
		render the view

		Parameters:
		root (object): root tkinter object
		"""
		if root is None:
			root = self.root
		tk.mainloop()
