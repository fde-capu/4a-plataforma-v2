# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import sys
from class_needle import *
from counter import *

g_verbose_mode = 1
global g_ref_file

if len(sys.argv) != 1:
	g_verbose_mode = 0
	vector = sys.argv[1:]
	for i in range(len(vector)):
		vector[i] = vector[i].strip("\"\',[]")
	vector = ",".join(vector)
	vector = "[" + vector + "]"
	count = count_vector_in_file(vector)
	print(count, end = "")
