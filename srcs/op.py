# # #
# # # helper operations for
# # # find a vector in a bitmap . fde-capu . 2012
# # # written for Python 3.7.3
# # #

class	op():
	def	xtoa(self):
		return str(self)
	def zero_index(self):
		return (self[1] - 1, self[0] - 1)
	def print_if_true(string, boolean):
		if boolean: print(string)
