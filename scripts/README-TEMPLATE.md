# PROJECT_NAME

by: AUTHOR_NAME (AUTHOR_EMAIL)

## Description

PROJECT_DESCRIPTION

## Requirements

-   Python 3.7+
-   FastAPI
-   Uvicorn

This project is using DB_TYPE.

This project is using [Poetry](https://python-poetry.org/) for dependency management. You can install the dependencies by running:

```bash
poetry install
```

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

## Running

To start the server, run the following command:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## Testing

To run the tests, run the following command:

```bash
PYTHONPATH=. pytest tests/units
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
