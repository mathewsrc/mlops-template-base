#!bin/bash

if [ "{{cookiecutter.use_mlflow}}" == "y" ]; then
    echo "Current directory: $(pwd)"
fi