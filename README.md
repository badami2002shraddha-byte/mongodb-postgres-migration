# MongoDB to PostgreSQL Data Migration

## Project Overview

This project demonstrates a data migration pipeline built with Python to transfer customer records from MongoDB to PostgreSQL.

The script reads customer documents from a MongoDB collection, inserts them into a PostgreSQL table, handles database errors, and validates the source and target record counts.

## Technologies Used

* Python
* MongoDB
* PostgreSQL
* PyMongo
* Psycopg2
* python-dotenv

## Project Structure

```text
mongodb_postgres_migration/
├── src/
│   └── migration.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Features

* Reads customer documents from MongoDB.
* Inserts records into PostgreSQL.
* Uses parameterized SQL queries.
* Handles duplicate customer IDs using `ON CONFLICT DO NOTHING`.
* Uses transactions and rollback for error handling.
* Loads database configuration from environment variables.
* Validates source and target record counts.

## Prerequisites

Install Python and ensure MongoDB and PostgreSQL are running locally.

## Setup Instructions

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd mongodb_postgres_migration
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root using the following template:

```dotenv
MONGO_URI=mongodb://localhost:27017/
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=migration_target
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_local_password
```

Replace `your_local_password` with your own PostgreSQL password. Never commit your real `.env` file.

### 4. Prepare the databases

Create a MongoDB database named `migration_demo` with a `customers` collection.

Create a PostgreSQL database named `migration_target` and a `customers` table with these columns:

* `customer_id` — INTEGER PRIMARY KEY
* `name` — VARCHAR(100)
* `email` — VARCHAR(150)
* `city` — VARCHAR(100)
* `age` — INTEGER

### 5. Run the migration

```bash
python src/migration.py
```

## Validation

The script compares the number of documents in the MongoDB source collection with the number of rows in the PostgreSQL target table.

During testing, five customer records were processed, and the source and target counts matched.

## Learning Outcomes

This project demonstrates database connectivity, ETL fundamentals, SQL insertion, transaction management, environment-variable configuration, error handling, and basic data validation.

## Future Improvements

* Incremental migration of new or updated records.
* Logging to a file.
* Data-quality checks.
* Automated tests.
* Improved validation of inserted and updated records.
