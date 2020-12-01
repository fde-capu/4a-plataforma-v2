FROM	alpine:latest
RUN		mkdir -p /app
COPY	main.py /app/
COPY	bitmap.json /app/
COPY	*.py /app/
EXPOSE	5000
COPY	init.sh /
ENTRYPOINT	["/init.sh"]
