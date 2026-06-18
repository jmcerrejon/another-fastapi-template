# PROJECT_NAME

by: AUTHOR_NAME (AUTHOR_EMAIL)

## Description

PROJECT_DESCRIPTION

## Requirements

-   Python 3.13+
-   FastAPI
-   Uvicorn

This project is using DB_TYPE.

This project is using [uv](https://docs.astral.sh/uv/) for dependency management. You can install the dependencies by running:

```bash
uv sync
```

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

3. Sync the dependencies:

    ```bash
    uv sync
    ```

## Running

To start the server, run the following command:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## Testing

To run the tests, run the following command:

```bash
uv run pytest tests/units
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
