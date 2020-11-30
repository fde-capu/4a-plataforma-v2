# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # # written for Python 3.7.3
# # #

import numpy as np
import json
import sys
import getopt
from op import *

# # #

g_range_min = 0
g_range_max = 15
g_verbose_mode = 1
global g_ref_file

# # #

def	count_vector_in_file(vector):
	g_ref_file = "/app/bitmap.json"
	try:
		with open(g_ref_file) as file:
			fullstr = file.read()
	except:
		g_ref_file = g_ref_file.replace("/app/", "")
		with open(g_ref_file) as file:
			fullstr = file.read()
	return count_vector_in_matrix(vector, fullstr)

def count_vector_in_matrix(vector, matrix):
	return str(find_vector_in_bmp_json(vector, matrix))

def	intro():
	op.print_if_true("Hello, bmp_matrix! by fde-capu", g_verbose_mode)

def vector_compare(vec_a, vec_b):
	if len(vec_a) == 0 or len(vec_b) == 0: return 0
	if len(vec_a) != len(vec_b): return 0
	return 1 if (np.array(vec_a) == np.array(vec_b)).all() else 0

def find_vector_in_bmp(needle, bitmap):
	if not needle.m: return 0
	found = 0
	if bitmap.n > 1: found += find_vector_in_bmp(needle, bmp(bitmap.matrix[1:,:]))
	if needle.m < bitmap.m:
		bmp_extract = bmp([bitmap.matrix[0,1:]])
		found += find_vector_in_bmp(needle, bmp_extract)
	extract = bitmap.get_vector_at_x_y((1, 1), needle.m)
	found += vector_compare(needle.vector, extract)
	return found

def find_vector_in_bmp_json(json_vector, json_matrix):
	return find_vector_in_bmp( \
		needle(np.array(json.loads(json_vector))), \
		bmp(np.array(json.loads(json_matrix))) \
		)

# # #

class	bmp(object):
	def	__init__(self, bmp, silent = 1):
		self.m, self.n = (0, 0)
		self.matrix = np.array([[]])
		try:
			if len(bmp) == 0:
				raise AttributeError
			rectangle_len = 0
			for x in bmp:
				if rectangle_len == 0: rectangle_len = len(x)
				if len(x) == 0 or len(x) != rectangle_len:
					raise AttributeError
		except AttributeError:
			op.print_if_true("Matrix error.", g_verbose_mode)
		else:
			self.matrix = np.array(bmp)
			if self.matrix.ndim > 1:
				self.n, self.m = self.matrix.shape
			else:
				self.n = 1
				self.m = len(self.matrix)
			if not silent: intro(); op.print_if_true(self, g_verbose_mode)
	def __str__(self):
		return self.show_me()
	def show_me(self):
		bmp_str = "This is a matrix of m = " \
			+ op.xtoa(self.m) + ", n = " + op.xtoa(self.n) \
			+ ", transposed for readability:\n"
		bmp_str += op.xtoa(self.matrix.transpose()) + ""
		return bmp_str
	def	element(self, tup_xy):
		x, y = op.zero_index(tup_xy)
		if x + 1 <= 0 or y + 1 <= 0:
			return "Invalid zero or negative input."
		if x + 1 > self.n or y + 1 > self.m: return "Out of bound."
		return self.matrix[x][y]
	def	get_vector_at_x_y(self, tup_xy, length):
		x, y = op.zero_index(tup_xy)
		if length <= 0: return "Invalid length."
		if x + 1 <= 0 or y + 1 <= 0:
			return "Invalid zero or negative input."
		if y > self.n: return "Invalid column."
		if y + length > self.m: return "Out of bound."
		return self.matrix[x, y:y + length]

class	needle(object):
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

# # #

if len(sys.argv) != 1:
	g_verbose_mode = 0
	vector = sys.argv[1:]
	for i in range(len(vector)):
		vector[i] = vector[i].strip("\"\',[]")
	vector = ",".join(vector)
	vector = "[" + vector + "]"
	count = count_vector_in_file(vector)
	print(count, end = "")
