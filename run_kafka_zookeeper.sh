#!/bin/bash -e

# Create network
docker network create platform-networks

# Up kafka and zookeeper
docker-compose up -d

echo "kafka and zookeeper ready!"