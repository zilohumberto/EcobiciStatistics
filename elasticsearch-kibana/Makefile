build:
	docker build --no-cache -t elasticsearch-kibana .

create:
	docker run --name=kibana -d -p 8000:8000 -p 9200:9200 elasticsearch-kibana

start:
	docker container start kibana

stop:
	docker container stop kibana

restart:
	docker container restart kibana

rm:
	docker rm kibana
