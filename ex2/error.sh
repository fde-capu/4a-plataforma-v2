#!/bin/sh
docker exec neqvecsinbmp ps -a
docker logs neqvecsinbmp
curl localhost:5000
curl -d "[2]" localhost:5000
curl -d "[4, 0, 0]" localhost:5000
