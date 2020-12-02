from flask import Flask, jsonify, request
from main import *
import json
import re

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	vector = str(json.loads(request.get_data().decode('utf-8')))
	count = count_vector_in_file(vector)
	return jsonify(count)

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
