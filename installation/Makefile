
build:
	docker build -t ecobici:1.0.0 .

create:
	docker run -it --rm --name cecobici --network host -v /home/ecobici:/home/ecobici ecobici:1.0.0

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
