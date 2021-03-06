# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import sys
import re
from class_needle import *
from counter import *

def	validate_or_empty(vec):
	vec = [re.sub(',', '', v) for v in vec]
	vec_full = ','.join(vec)
	vec_full = re.sub('[ \'\"]', '', vec_full)
	if not re.compile('\[|\]').search(vec_full):
		vec_full = '[' + vec_full + ']'
	try:
		validate = json.loads(vec_full)
	except:
		return ''
	if type(validate) != list \
	or len(validate) == 0 \
	or validate != [v for v in validate if type(v) == int and 0 <= v and v <= 15]:
		return ''
	return vec_full

if len(sys.argv) != 1:
	vector = validate_or_empty(sys.argv[1:])
	if vector == '':
		sys.exit('Invalid input.')
	if not re.compile('\[|\]').search(vector):
		vector = '[' + vector + ']'
	count = count_vector_in_file(vector)
	if count == '':
		sys.exit('Empty response.')
	print(count, end = '')
else:
	print('Read the README.md file.')
