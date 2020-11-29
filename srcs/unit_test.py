# # #
# # # unit test for
# # # find a vector in a bitmap . fde-capu . 2012
# # # written for Python 3.7.3
# # #

from bmp_matrix import *
from op import *
import os
import json
import subprocess

# # #

json_input_bmp = '[		\
	[11,  7,  5,  9],	\
	[ 6,  1,  0,  2],	\
	[10, 15,  3,  8]	\
	]'

json_input_bmp_other = '[				\
	[	2,	5,	7,	9,	1,	0,	15	],	\
	[	6,	3,	2,	5,	7,	8,	5	],	\
	[	1,	0,	15,	0,	4,	4,	3	],	\
	[	7,	8,	7,	5,	2,	5,	7	],	\
	[	3,	1,	0,	15,	7,	8,	5	],	\
	[	0,	4,	4,	8,	7,	5,	7	]	\
	]'

json_input_vec = '[2, 5, 7]'

test_get_element = [(2, 1), (7, 7), (2, -3), (0, 4), (4, 3), (1, 3)]

vector_lengths = [-2, 0, 1, 2, 3, 7, 4]

test_needle = [ \
	[3], \
	[5, 7], \
	[0, 4, 4], \
	[5, -1, 7], \
	[1, 0, 15], \
	[7, 8, 16], \
	[7, 8, 5], \
	[7, 5], \
	[] \
	]

# # #

g_not_silent = 0

# # #

print("\nUnit test")

print ("\nLoading local bitmap (no error expected). Raw.")
local_bmp = bmp(json.loads(json_input_bmp), g_not_silent)
local_bmp_other = bmp(json.loads(json_input_bmp_other), g_not_silent)
print (" Done.")

print ("\nLoading local vector needle (no error expected). Raw.")
local_vec = needle(json.loads(json_input_vec), g_not_silent)
print (" Done.\n")

print ("Load empty vector:", needle([]), "done.\n")

for t in test_get_element:
	element = local_bmp.element(t)
	print("Test get element (x, y) = " + op.xtoa(t) + ": " \
		+ op.xtoa(element))
print ("Done.\n")

for l in vector_lengths:
	for t in test_get_element:
		vec = local_bmp.get_vector_at_x_y(t, l)
		print("Get vector at " + op.xtoa(t) + ",\tlength " \
			+ op.xtoa(l) + "\t" + op.xtoa(vec))
print ("Done.\n")

for n in test_needle:
	print("Init vector " + op.xtoa(n) + ". ", end = "")
	t_needle = needle(n)
	print (op.xtoa(t_needle))
print ("Done.\n")

print("Vector compare:")
for n in test_needle:
	print("vector " + op.xtoa(n) + ". ", end = "")
	print("found" if vector_compare(n, n) else "-", end = "")
	print("found" if vector_compare(n, [1, 0, 15]) else "-")
print ("Done.\n")

print("Find vector in bmp:")
print(str(local_bmp), ":::")
for n in test_needle:
	print(n, " -> ", end = " ")
	print(find_vector_in_bmp(needle(n), local_bmp))

print("Find vector in bmp_other:")
print(str(local_bmp_other), ":::")
for n in test_needle:
	print(n, " -> ", end = " ")
	print(find_vector_in_bmp(needle(n), local_bmp_other))

print("Find from json inputs:")
print(" ::: \n", json_input_vec, "\n ::: \n", json.loads(json_input_bmp))
print("==>", find_vector_in_bmp_json(json_input_vec, json_input_bmp))
print("==>", count_vector_in_matrix(json_input_vec, json_input_bmp))
print(" ::: \n", json_input_vec, "\n ::: \n", json.loads(json_input_bmp_other))
print("==>", find_vector_in_bmp_json(json_input_vec, json_input_bmp_other))
print("==>", count_vector_in_matrix(json_input_vec, json_input_bmp_other))

print("Find from file:")
print(" ::: ", json_input_vec, " :::")
print("==>", count_vector_in_file(json_input_vec))

print("Find from CLI: plain list:")
for n in test_needle:
	cmd = "python3 bmp_matrix.py " + str(n)
	print("`" + cmd + "`")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(">>", test)
