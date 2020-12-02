# # #
# # # unit test for
# # # find a vector in a bitmap . fde-capu . 2012
# # #

from main import *
from op import *
import os
import json
import subprocess

# # #

test_needle = [ \
	[3], \
	[5, 7], \
	[0, 4, 4], \
	[1, 0, 15], \
	[7, 8, 5], \
	[7, 5], \
]

answ_needle = [ \
	3, \
	4, \
	2, \
	3, \
	2, \
	2, \
	0,
]

wrong_formats = [ \
	"o 4 4", \
	"[[2, 5]]", \
	"[5, , 7]", \
	"[7 9, 1", \
	"5 ] 2", \
	[7, 8, 16], \
	"[ 5 , [ 7 ]", \
	[5, -1, 7], \
	[[5, 7]], \
	[], \
	"[]", \
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

print("\nFind from CLI: wrong formatting (error expected), double quotes:")
for n in wrong_formats:
	test = ""
	cmd = "python3 main.py \"" + str(n) + "\""
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	test = "OK"
	else:	alert(test)

print("\nFind from CLI: wrong formatting (error expected), no quotes:")
for n in wrong_formats:
	test = ""
	cmd = "python3 main.py " + str(n) + ""
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	test = "OK"
	else:	alert(test)

print("\nFind from CLI: plain list:")
for i, n in enumerate(test_needle):
	test = ""
	cmd = "python3 main.py " + str(n) + ""
	print("`" + cmd + "`", end = " ", flush = True)
	try:	ans = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == ans:
		print(" >>", answ_needle[i])
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + ans)

print("\nFind from CLI: plain list, no brackets:")
for i, n in enumerate(test_needle):
	test = ""
	cmd = "python3 main.py " + str(n) + ""
	cmd = cmd.replace("[", "").replace("]", "")
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == test:
		print(" >>", test)
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + test)

print("\nFind from CLI: plain list, no brackets, no comma:")
for i, n in enumerate(test_needle):
	test = ""
	cmd = "python3 main.py " + str(n) + ""
	cmd = cmd.replace("[", "").replace("]", "").replace(",", "")
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == test:
		print(" >>", test)
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + test)

print("\nFind from CLI: in string list (json):")
for i, n in enumerate(test_needle):
	test = ""
	cmd = "python3 main.py \"" + str(n) + "\""
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == test:
		print(" >>", test)
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + test)

print("\nFind from CLI: plain list, no brackets:")
for i, n in enumerate(test_needle):
	test = ""
	cmd = "python3 main.py \"" + str(n) + "\""
	cmd = cmd.replace("[", "").replace("]", "")
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == test:
		print(" >>", test)
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + test)

print("\nFind from CLI: plain list, no brackets, no comma:")
for i, n in enumerate(test_needle):
	test = ""
	cmd = "python3 main.py \"" + str(n) + "\""
	cmd = cmd.replace("[", "").replace("]", "").replace(",", "")
	print("`" + cmd + "`", end = " ", flush = True)
	try:	test = subprocess.check_output(cmd.split()).decode('utf-8')
	except:	alert("Runtime error.")
	if str(answ_needle[i]) == test:
		print(" >>", test)
	else:
		alert("Fail: " + str(answ_needle[i]) + ": got " + test)
