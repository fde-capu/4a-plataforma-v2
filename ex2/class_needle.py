# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import sys
import numpy as np

g_range_min = 0
g_range_max = 15

class	needle_init(object):
	def __init__(self, vector):
		self.m = 0
		self.vector = []
		try:
			if len(vector) == 0:
				raise AttributeError
		except AttributeError:
			sys.exit("Vector is empty.")
		else:
			self.vector = np.array(vector)
			self.m = len(self.vector)
	def __str__(self):
		return self.show_me()
	def show_me(self):
		return str(self.vector)
