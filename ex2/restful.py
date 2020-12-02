# # #
# # # count a vector in a bitmap . fde-capu . 2012
# # #

import sys
from flask import Flask, jsonify, request
import json
import re
from counter import count_vector_in_file

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	try:	vector = str(json.loads(request.get_data().decode('utf-8')))
	except:	return jsonify('0')
	count = count_vector_in_file(vector)
	return jsonify(count)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
