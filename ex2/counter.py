# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import json
import numpy as np
from class_needle import *
from class_matrix import *

def	count_vector_in_file(vector):
	ref_file = "/app/bitmap.json"
	try:
		with open(ref_file) as file:
			fullstr = file.read()
	except:
		ref_file = ref_file.replace("/app/", "")
		with open(ref_file) as file:
			fullstr = file.read()
	return count_vector_in_matrix(vector, fullstr)

def count_vector_in_matrix(vector, matrix):
	return str(find_vector_in_bmp_json(vector, matrix))

def vector_compare(vec_a, vec_b):
	if len(vec_a) == 0 or len(vec_b) == 0: return 0
	if len(vec_a) != len(vec_b): return 0
	return 1 if (np.array(vec_a) == np.array(vec_b)).all() else 0

def find_vector_in_bmp(needle, bitmap):
	if not needle.m: return 0
	found = 0
	if bitmap.n > 1:
		found += find_vector_in_bmp(needle, matrix_init(bitmap.matrix[1:,:]))
	if needle.m < bitmap.m:
		bmp_extract = matrix_init([bitmap.matrix[0,1:]])
		found += find_vector_in_bmp(needle, bmp_extract)
	extract = bitmap.get_vector_at_x_y((1, 1), needle.m)
	found += vector_compare(needle.vector, extract)
	return found

def find_vector_in_bmp_json(json_vector, json_matrix):
	return find_vector_in_bmp( \
		needle_init(np.array(json.loads(json_vector))), \
		matrix_init(np.array(json.loads(json_matrix))) \
		)
