
build:
	docker build --no-cache -t ecobici:1.0.0 .

create:
	docker run -itd --name cecobici -p 127.0.0.1:5000:5000 -v /home/ecobici/:/home/ecobici ecobici:1.0.0

start:
	docker container start cecobici

stop:
	docker container stop cecobici

restart:
	docker container restart cecobici

bash:
	docker exec -it cecobici bash

rm:
	docker rm cecobici
