SHELL := /bin/bash # Use bash syntax

install-dockertools:
	sudo apt-get update
	sudo apt-get install ca-certificates curl gnupg
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh ./get-docker.sh
	sudo apt-get install docker-compose
	sudo groupadd docker
	sudo usermod -aG docker $USER
	newgrp docker

install: install-dockertools

run:
	docker build --tag frontend -f hackathon_submission/frontend/Dockerfile .
	docker build --tag backend -f hackathon_submission/backend/Dockerfile .

	docker container create -p 8501:8501 -p 8000:8000 --name web frontend
	docker container create -p 8000:8000  --name server backend

	docker start web
	docker start server

uninstall:
	docker stop server
	docker stop web

	docker container rm server
	docker container rm web

	docker image rm frontend
	docker image rm backend

	docker network rm DiagnoEase_net
