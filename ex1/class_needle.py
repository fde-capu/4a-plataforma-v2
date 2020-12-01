# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import numpy as np

g_range_min = 0
g_range_max = 15

class	needle_init(object):
	def __init__(self, vector, silent = 1):
		self.m = 0
		self.vector = []
		try:
			if len(vector) == 0:
				raise AttributeError
			for r in vector:
				if r < g_range_min or r > g_range_max: raise IndexError
		except AttributeError:
			op.print_if_true("Vector is empty.", g_verbose_mode)
		except IndexError:
			op.print_if_true("error: vector out of range (" + str(g_range_min) \
				+ " to " + str(g_range_max) + ").", g_verbose_mode)
		else:
			self.vector = np.array(vector)
			self.m = len(self.vector)
		finally:
			if not silent: op.print_if_true ("Built " + op.xtoa(self.vector), \
				g_verbose_mode)
	def __str__(self):
		return self.show_me()
	def show_me(self):
		return op.xtoa(self.vector)
