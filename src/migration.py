import os
import psycopg2
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["migration_demo"]
collection = db["customers"]
customers=collection.find()
for customer in customers:
    print(customer)
pg_conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
print("PostgreSQL connection successful!")
cursor = pg_conn.cursor()
insert_query="""
INSERT INTO customers
(customer_id, name, email, city, age)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (customer_id) DO NOTHING
"""
migrated_count = 0
try:
    for customer in collection.find():
        cursor.execute(
            insert_query,
            (
                customer["customer_id"],
                customer["name"],
                customer["email"],
                customer["city"],
                customer["age"]
            )
        )
        migrated_count += 1
    pg_conn.commit()
    source_count = collection.count_documents({})
    cursor.execute("SELECT COUNT(*) FROM customers")
    target_count = cursor.fetchone()[0]
    print("Data migration completed successfully!")
    print("Total source records processed:", migrated_count)
    if source_count == target_count:
        print("Validation successful: Source and target counts match.")
    else:
        print("Validation failed: Source and target counts do not match.")
        print("MongoDB count:", source_count)
        print("PostgreSQL count:", target_count)

except Exception as e:
    pg_conn.rollback()
    print("Migration failed:", e)

finally:
    cursor.close()
    pg_conn.close()
    client.close()

