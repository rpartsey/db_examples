import psycopg2

params = {
    "user": "postgres",
    "password": "postgres",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "postgres"
}

# Connect to an existing database
conn = psycopg2.connect(**params)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

# Using 'with' context manager
# 1
# with psycopg2.connect(**params) as conn:
#     with conn.cursor() as cur:
#         cur.execute("SELECT NOW();")
#         print(cur.fetchone())

# 2
# conn = psycopg2.connect(**params)
# try:
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute("SELECT NOW();")
#             print(cur.fetchone())
# finally:
#     conn.close()
