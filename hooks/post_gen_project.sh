# Install Poetry
chmod +x install_poetry.sh
./install_poetry.sh


if [ "{{cookiecutter.use_mlflow}}" == "y" ]; then
    chmod +x setup_mlflow.sh
    ./setup_mlflow.sh
fi