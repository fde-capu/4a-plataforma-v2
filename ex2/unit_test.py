# # #
# # # unit test for
# # # find a vector in a bitmap . fde-capu . 2012
# # # restful api version
# # #

from main import *
from op import *
import os
import json
import subprocess

# # #

test_needle = [ \
	[5, 7], \
	[0, 4, 4], \
	[1, 0, 15], \
	[7, 8, 5], \
	[7, 5], \
	[3], \
	[11, 7], \
	[2, 5, 7], \
]


answ_needle = [ \
	4, \
	2, \
	3, \
	2, \
	2, \
	3, \
	0, \
	3, \
]

wrongs = [ \
	[], \
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

print("\nFind from CLI: in string list (json):")
for i, n in enumerate(test_needle):
	test = ""
	nn = str(n)
	cmd = "curl -sd \"" + nn + "\" localhost:5000"
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = json.loads(subprocess.check_output(['curl', '-sd', nn, 'localhost:5000']).decode('utf-8'))
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == test:
		print(" >>", test)
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + str(test))
