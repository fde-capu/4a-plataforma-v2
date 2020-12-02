#!/bin/sh
docker rm -f neqvecsinbmp
#docker rmi -f c_vec_in_mat

docker build -t c_vec_in_mat .
docker run -p 5000:5000 -d --name neqvecsinbmp c_vec_in_mat
echo "Sleeping 10 seconds"
sleep 10
python3 ./unit_test.py
