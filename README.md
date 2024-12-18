# Another FastAPI Template

This is my custom template project for a simple FastAPI application.

## Description

This template provides a basic setup for a FastAPI application.

## Requirements

-   Python 3.12+
-   FastAPI
-   Uvicorn
-   SQLAlchemy
-   Poetry (optional)
-   Pytest

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

4. Copy .env.example to .env and modify the values:

```bash
cp .env.example .env
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

## Running

To start the server, run the following command:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## Docker

You have a containerized version of the app. To build the image, run:

```sh
docker build -t fastapi-template . && docker run -d -p 8000:8000 --name fastapi-container fastapi-template
```

## Testing

To run the tests, run the following command:

```bash
PYTHONPATH=. pytest
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
-   [x] Add .env support.
-   [x] Add SQLAlchemy support.
-   [x] Add Poetry.
-   [x] Testing.
-   [x] Add Dockerfile.
-   [x] Log system.
-   [ ] Authentication.
-   [ ] Modify scripts/boilerplate-customizer.sh to add more options.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

-   Made with ❤️ and ☕️ by [Jose Cerrejon](mailto:ulysess@gmail.com).
-   Inspired on posts by [@aberrospic1](https://medium.com/@aberrospic1/crud-operations-with-fastapi-c2de026e5862) & [@lou_adam](https://medium.com/@lou_adam/best-practices-for-building-deploying-rest-api-as-data-engineer-concrete-example-with-fastapi-84522745a9f7#7dfc).
