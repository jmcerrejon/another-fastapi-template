# Another FastAPI Template

This is my custom template project for a simple FastAPI application.

## Description

This template provides a basic setup for a FastAPI application.

## Requirements

-   Python 3.13+
-   [uv](https://docs.astral.sh/uv/) (recommended)
-   FastAPI
-   Uvicorn
-   SQLAlchemy
-   Pytest

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jmcerrejon/another-fastapi-template.git
cd another-fastapi-template
```

2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Sync the dependencies (creates `.venv` and installs everything pinned in `uv.lock`):

```bash
uv sync
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
uv run uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## Docker

You have a containerized version of the app. To build the image, run:

```sh
docker build -t fastapi-template . && docker run -d -p 8000:8000 --name fastapi-container fastapi-template
```

## Testing

To run the tests, run the following command:

```bash
uv run pytest
```

## Using uv

To install and use [uv](https://docs.astral.sh/uv/) in the project, follow these steps:

1. Install uv (see the [installation guide](https://docs.astral.sh/uv/getting-started/installation/)).

2. Sync the dependencies (creates `.venv` and installs everything pinned in `uv.lock`):

```bash
uv sync
```

3. To add a new dependency, use one of the following commands:

```bash
uv add <package_name>              # runtime dependency
uv add --group dev <package_name>  # dev dependency
```

4. To upgrade all dependencies to the latest allowed versions and refresh `uv.lock`:

```bash
uv lock --upgrade
uv sync
```

5. To run the project using uv, prepend `uv run` to any command:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## TODO

-   [x] Add Database support (default: sqlite).
-   [x] Add .env support.
-   [x] Add SQLAlchemy support.
-   [x] Add uv.
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
