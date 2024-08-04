# MLOps cookiecutter template

### To use this cookiecutter template use the following command on Terminal:

```
pip install cookiecutter
cookiecutter gh:mathewsrc/mlops-template-base
```

### Then use Git `init` command:

```
cd {{ cookiecutter.repository }}
git init
```

### Finally enable GitHub Pages Workflow:
- Navigate to your repository settings on GitHub: "Settings" -> "Actions" -> "General."
- Under "Workflow permissions," ensure "Read and write permissions" is selected.
This allows the workflow to automatically publish your documentation.

### Use the provided Invoke tasks to manage your development workflow:

- invoke installs: Install dependencies and pre-commit hooks.
- invoke formats: Format your code.
- invoke checks: Run code quality, type, security, and test checks.
- invoke docs: Generate API documentation.
- invoke containers: Build and run your Docker image.