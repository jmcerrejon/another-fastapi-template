# Another FastAPI Template

This is my custom template project for a simple FastAPI application.

## Description

This template provides a basic setup for a FastAPI application with a health endpoint to check the server status.

## Requirements

-   Python 3.12+
-   FastAPI
-   Uvicorn
-   SQLAlchemy

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jmcerrejon/another-fastapi-template.git
cd another-fastapi-template
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

If you want to use the customizer script, run the following command:

```bash
./scripts/boilerplate-customizer.sh
```

If you want to start a new project once you have cloned the repository, remove the `.git` directory and start a new git repository. But, maybe you want to get updates from this repository. You can add it as a remote upstream:

```bash
rm -rf .git
git init
# (Optional) Add the remote repository as upstream
git remote add upstream git@github.com:jmcerrejon/another-fastapi-template.git
```

When you want to get updates from this repository:

```bash
git pull upstream main
```

Thank you! ❤️

## Running

To start the server, run the following command:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
# Go to http://127.0.0.1:8000/health
```

## Testing

To run the tests, run the following command:

```bash
PYTHONPATH=. pytest tests/units
```

## Using Poetry

To install and use Poetry in the project, follow these steps:

1. Install Poetry:

```bash
pip install poetry
```

2. Install the dependencies using Poetry:

```bash
poetry install
```

3. To add a new dependency, use the following command:

```bash
poetry add <package_name>
```

4. To run the project using Poetry, use the following command:

```bash
poetry run uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## TODO

-   [x] Add Database support (default: sqlite).
-   [ ] Add Poetry.
-   [ ] Modify scripts/boilerplate-customizer.sh to add more options.
-   [ ] Add Dockerfile.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

-   Made with ❤️ and ☕️ by [Jose Cerrejon](mailto:ulysess@gmail.com).
