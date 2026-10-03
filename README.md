# MongoDB to PostgreSQL Data Migration

## Project Overview

This project demonstrates a Python-based ETL (Extract, Transform, Load) pipeline that migrates customer records from MongoDB to PostgreSQL.

The script extracts customer documents from MongoDB, loads them into a PostgreSQL table, handles database errors using transactions, and validates the migration by comparing source and target record counts.

## Technologies Used

* Python
* MongoDB
* PostgreSQL
* PyMongo
* Psycopg2
* python-dotenv
* Git and GitHub

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

* Connects to MongoDB and PostgreSQL.
* Extracts customer records from MongoDB.
* Inserts customer records into PostgreSQL using parameterized SQL queries.
* Handles duplicate customer IDs using `ON CONFLICT DO NOTHING`.
* Uses database transactions and rollback for error handling.
* Loads database configuration from environment variables.
* Validates source and target record counts.
* Closes database connections after execution.

## Prerequisites

Install or configure the following:

* Python 3.10 or later
* MongoDB running locally
* PostgreSQL running locally
* Git
* MongoDB Compass and pgAdmin 4 (optional, for database inspection)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/badami2002shraddha-byte/mongodb-postgres-migration.git
cd mongodb-postgres-migration
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```dotenv
MONGO_URI=mongodb://localhost:27017/
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=migration_target
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_local_password
```

Replace `your_local_password` with your own PostgreSQL password.

**Security note:** Never commit your real `.env` file or database credentials to GitHub.

### 4. Prepare the Source Database

In MongoDB, create or use the following database and collection:

* Database: `migration_demo`
* Collection: `customers`

Each customer document should contain these fields:

* `customer_id`
* `name`
* `email`
* `city`
* `age`

### 5. Prepare the Target Database

Create a PostgreSQL database named `migration_target`.

Inside that database, create a table named `customers` using the following SQL:

```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(100),
    age INTEGER
);
```

### 6. Run the Migration

From the project root directory, run:

```bash
python src/migration.py
```

The script will connect to both databases, read customer documents from MongoDB, insert records into PostgreSQL, and validate the record counts.

## Validation

After migration, the script compares the number of documents in the MongoDB source collection with the number of rows in the PostgreSQL target table.

The project was tested locally with five customer records. The source and target record counts matched successfully.

**Note:** The current validation compares total record counts. Matching counts alone does not guarantee that every field in every record is identical.

## Error Handling

The project includes:

* Exception handling for migration errors.
* Transaction rollback if an error occurs during migration.
* Duplicate-key handling through `ON CONFLICT DO NOTHING`.
* Cleanup of database connections after execution.

## Learning Outcomes

This project demonstrates practical experience with:

* ETL pipeline fundamentals.
* MongoDB and PostgreSQL connectivity.
* SQL data insertion.
* Python database libraries.
* Environment-variable configuration.
* Transaction management and error handling.
* Basic data validation.
* Git and GitHub version control.

## Future Improvements

* Implement incremental migration for new or updated records.
* Add structured logging to a file.
* Compare individual source and target records.
* Add automated tests.
* Track newly inserted, skipped, and failed records separately.
* Improve data-quality checks and validation reporting.

## Author

Shraddha Badami

GitHub: https://github.com/badami2002shraddha-byte
