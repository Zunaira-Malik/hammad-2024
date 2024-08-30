
## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Python 3.9+
- Docker
- Docker Compose

## Setup Instructions

### 1. Create and Activate a Virtual Environment

First, create a virtual environment to isolate your project dependencies:

```bash
python3 -m venv env
```

Activate the virtual environment:

- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```
- On Windows:
  ```bash
  .\env\Scripts\activate
  ```

### 2. Install Required Packages

Install all the necessary packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Run Docker Compose

Start the Docker containers using Docker Compose:

```bash
docker-compose up -d
```

This will set up the necessary services (e.g., database, cache) as defined in your `docker-compose.yml`.

### 4. Run Migrations

Apply database migrations to set up the database schema:

```bash
python3 manage.py migrate
```

### 5. Run the Project

Finally, start the Django development server:

```bash
python3 manage.py runserver
```

