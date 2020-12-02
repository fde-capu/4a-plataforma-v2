# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import numpy as np
from op import *

class	matrix_init(object):
	def	__init__(self, bmp):
		self.m, self.n = (0, 0)
		self.matrix = np.array([[]])
		self.fail = 0
		try:
			if len(bmp) == 0:
				raise AttributeError
			rectangle_len = 0
			for x in bmp:
				if rectangle_len == 0: rectangle_len = len(x)
				if len(x) == 0 or len(x) != rectangle_len:
					raise AttributeError
		except AttributeError:
			self.fail = 1
		else:
			self.matrix = np.array(bmp)
			if self.matrix.ndim > 1:
				self.n, self.m = self.matrix.shape
			else:
				self.n = 1
				self.m = len(self.matrix)
	def	element(self, tup_xy):
		x, y = op.zero_index(tup_xy)
		if x + 1 <= 0 or y + 1 <= 0:
			return 'Invalid zero or negative input.'
		if x + 1 > self.n or y + 1 > self.m: return 'Out of bound.'
		return self.matrix[x][y]
	def	get_vector_at_x_y(self, tup_xy, length):
		x, y = op.zero_index(tup_xy)
		if length <= 0: return 'Invalid length.'
		if x + 1 <= 0 or y + 1 <= 0:
			return 'Invalid zero or negative input.'
		if y > self.n: return 'Invalid column.'
		if y + length > self.m: return 'Out of bound.'
		return self.matrix[x, y:y + length]
