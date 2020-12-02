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
		self.fail = 0
		try:
			if len(vector) == 0:
				raise AttributeError
		except AttributeError:
			self.fail = 1
		else:
			self.vector = np.array(vector)
			self.m = len(self.vector)
