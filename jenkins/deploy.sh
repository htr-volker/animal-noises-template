#!/bin/bash
project_name=bmi_stuff

 
# Build server
docker build -t ${project_name}_server server

# Build bmi_api
docker build -t ${project_name}_api bmi_api
docker build -t ${project_name}_apiheight height_api
docker build -t ${project_name}_apiweight weight_api

# Create network
 docker network create ${project_name}_network

# Run containers
docker run -d \
    -p 5000:5000 \
    --name ${project_name}_server \
    --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    --name ${project_name}_api \
    --network ${project_name}_network \
    ${project_name}_api

docker run -d \
    --name ${project_name}_apiheight \
    --network ${project_name}_network \
    ${project_name}_apiheight

docker run -d \
    --name ${project_name}_apiweight \
    --network ${project_name}_network \
    ${project_name}_apiweight