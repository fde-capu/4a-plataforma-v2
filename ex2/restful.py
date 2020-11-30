from flask import Flask, jsonify, request
from bmp_matrix import *
import json
import re

def	treat_many_ways(full_str):
	vector = full_str.decode('utf-8')
	vector = re.sub('["\"\'\,\[\]\ ]+', " ", vector)
	vector = vector.strip(" ")
	vector = re.sub(" ", ",", vector)
	vector = "[" + vector + "]"
	return vector

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	vector = treat_many_ways(request.get_data())
	return jsonify(count_vector_in_file(vector))

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
