#!/bin/bash

sudo apt update
sudo apt install -y curl jq

# Install Docker
curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins

# Install Docker Compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Ansible
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
sudo apt install python3-pip -y
pip3 install --user ansible
ansible --version

# Docker login
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD
