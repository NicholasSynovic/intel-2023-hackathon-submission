SHELL := /bin/bash # Use bash syntax

install-python:
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt install python3.8
	sudo apt install python3-pip

install-python-packages:
	pip install pandas numpy

install-dockertools:
	sudo apt-get update
	sudo apt-get install ca-certificates curl gnupg
	sudo install -m 0755 -d /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	sudo chmod a+r /etc/apt/keyrings/docker.gpg
	echo \
		"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
		"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
		sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
	sudo apt-get install docker.io
	sudo apt-get install docker-compose
	sudo groupadd docker
	sudo usermod -aG docker $USER
	newgrp docker

install-tools: install-python install-python-packages install-dockertools

launch:
	docker-compose -f docker-compose.yml -p full up
