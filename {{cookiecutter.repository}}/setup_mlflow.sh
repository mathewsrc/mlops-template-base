#!/bin/bash

# Add MLflow to Poetry dependencies
poetry add mlflow

# Create docker-compose.yml file
cat << EOF > docker-compose.yml
version: '3'
services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.10.0
    ports:
      - 5000:5000
    environment:
      - MLFLOW_HOST=0.0.0.0
    command: mlflow server
EOF

echo "Docker Compose file for MLflow has been created."