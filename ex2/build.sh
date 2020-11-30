#!/bin/sh
docker rm -f neqvecsinbmp
docker rmi -f c_vec_in_mat

docker build -t c_vec_in_mat .
docker run -p 5000:5000 -d --name neqvecsinbmp c_vec_in_mat

docker images -a
docker ps -a

wait(3)
curl localhost:5000
