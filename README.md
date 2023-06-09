# Journal API

[![Build Status](https://img.shields.io/github/workflow/status/carlsmith101/journal-api/CI)](https://github.com/carlsmith101/journal-api/actions/workflows/ci.yml)

This is a RESTful API for a journal application built using Flask and Flask-RESTX. It provides endpoints to manage journal entries and track various metrics related to personal well-being.

## Installation

To run the Journal API locally using Docker, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/carlsmith101/journal-api.git
   cd journal-api
   ```

2. Make sure you have Docker installed on your machine.

3. Build and run the Docker containers (in detached mode):
   ```
   docker-compose up -d
   ```

The Journal API should now be up and running on `http://localhost:5004`.

## Endpoints

The following endpoints are available in the Journal API:

- **GET /ping**: Returns a simple ping response to check the API status.
- **POST /entries**: Create a new journal entry.
- **GET /entries**: Get a list of all journal entries.
- **GET /entries/{entry_date}**: Get a specific journal entry by entry date.

For detailed information about each endpoint, including request/response formats and examples, you can refer to the API documentation available at `http://localhost:5004` when the application is running.

## Testing

The Journal API includes unit tests and integration tests to ensure its functionality. To run the tests, use the following command:

```
docker-compose exec api pytest
```

The tests use the `pytest` framework and can be found in the `tests/` directory.

---
