#!/bin/sh
docker exec neqvecsinbmp ps -a
docker logs neqvecsinbmp
cat ./bitmap.json
echo "Empty request:"
curl localhost:5000
t="[2]";		echo -n "$t\t"; curl -d "$t" localhost:5000
t="[0, 4, 4]";	echo -n "$t\t"; curl -d "$t" localhost:5000
t="2, 5, 7";	echo -n "$t\t"; curl -d "$t" localhost:5000
t="5 7";		echo -n "$t\t"; curl -d "$t" localhost:5000
t="\"7    5\"";	echo -n "$t\t"; curl -d "$t" localhost:5000
