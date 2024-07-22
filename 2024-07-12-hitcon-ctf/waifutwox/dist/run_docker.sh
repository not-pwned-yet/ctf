#!/bin/bash

# Stop and remove the existing container if it exists
if [ $(sudo docker ps -a -q --filter "name=my-docker-container") ]; then
    sudo docker stop my-docker-container
    sudo docker rm my-docker-container
fi

# Run the new container
sudo docker run -it --name my-docker-container my-docker-image

