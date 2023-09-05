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
	docker network create DiagnoEase_net

	# docker build --tag frontend -f hackathon_submission/frontend/Dockerfile .
	# docker build --tag backend -f hackathon_submission/backend/Dockerfile .

	docker container create -p 8501:8501 --ip "172.22.0.2/16" --name web frontend
	docker container create -p 8000:8000 --ip "172.22.0.3/16" --name server backend

	docker start web
	docker start server

	docker network connect DiagnoEase_net web
	docker network connect DiagnoEase_net server
