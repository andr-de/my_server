build: Dockerfile
	docker build . -t my_server

stop:
	
	docker stop my_server

start:
	docker run -d --rm --name=my_server -p 65432:65432 my_server:1