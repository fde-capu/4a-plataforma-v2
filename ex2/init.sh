#!/bin/sh
touch /COUNT_VECTOR_IN_MATRIX_CONTAINER
apk update
apk add python3 py3-numpy py3-flask
echo "count_vector_in_matrix rest api server up and running." > /app/index.html
python3 /app/restful.py &
tail -f /dev/null
