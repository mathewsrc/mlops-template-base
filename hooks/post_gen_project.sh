#!bin/bash

if [ "{{cookiecutter.use_mlflow}}" == "y" ]; then
    cd {{cookiecutter.repository}}
    chmod +x setup_mlflow.sh
    ./setup_mlflow.sh
fi