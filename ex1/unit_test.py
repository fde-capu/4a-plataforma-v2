# # #
# # # unit test for
# # # find a vector in a bitmap . fde-capu . 2012
# # # written for Python 3.7.3
# # #

from main import *
g_ref_file = "bitmap.json"
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
	[	0,	4,	4,	8,	7,	5,  7	]	\
	]'

json_inconsistent_bmp = '[[1], [1, 2]]'

json_input_vec = '[2, 5, 7]'

test_get_element = [(2, 1), (7, 7), (2, -3), (0, 4), (4, 3), (1, 3)]

vector_lengths = [-2, 0, 1, 2, 3, 7, 4]

test_needle = [ \
	[3], \
	[[5, 7]], \
	[0, 4, 4], \
	[5, -1, 7], \
	[1, 0, 15], \
	[7, 8, 16], \
	[7, 8, 5], \
	[7, 5], \
	[] \
	]
wrong_formats = [ \
	"o 4 4", \
	"[[2, 5]]", \
	"[5, , 7]", \
	"[7 9, 1", \
	"5 ] 2", \
	"[ 5 , [ 7 ]", \
	"7 9, 1", \
	"", \
]

# # #

g_not_silent = 0
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# # #

def		alert(str):
	print (bcolors.FAIL + ">>> " + str + " <<<" + bcolors.ENDC)
	return

print("\nUnit test")

print("Find from CLI: wrong formatting (error expected):")
for n in wrong_formats:
	cmd = "python3 main.py \"" + n + "\""
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	test = "OK"
	else:	alert(test)

exit()

print("Find from CLI: plain list:")
for n in test_needle:
	cmd = "python3 main.py " + str(n) + ""
	print("`" + cmd + "`", end = "")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(" >>", test)

print("Find from CLI: plain list, no brackets:")
for n in test_needle:
	cmd = "python3 main.py " + str(n) + ""
	cmd = cmd.replace("[", "").replace("]", "")
	print("`" + cmd + "`", end = "")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(" >>", test)

print("Find from CLI: plain list, no brackets, no comma:")
for n in test_needle:
	cmd = "python3 main.py " + str(n) + ""
	cmd = cmd.replace("[", "").replace("]", "").replace(",", "")
	print("`" + cmd + "`", end = "")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(" >>", test)

print("Find from CLI: in string list (json):")
for n in test_needle:
	cmd = "python3 main.py \"" + str(n) + "\""
	print("`" + cmd + "`", end = "")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(" >>", test)

print("Find from CLI: plain list, no brackets:")
for n in test_needle:
	cmd = "python3 main.py \"" + str(n) + "\""
	cmd = cmd.replace("[", "").replace("]", "")
	print("`" + cmd + "`", end = "")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(" >>", test)

print("Find from CLI: plain list, no brackets, no comma:")
for n in test_needle:
	cmd = "python3 main.py \"" + str(n) + "\""
	cmd = cmd.replace("[", "").replace("]", "").replace(",", "")
	print("`" + cmd + "`", end = "")
	test = subprocess.check_output(cmd.split()).decode('utf-8')
	print(" >>", test)
