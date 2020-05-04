from psycopg2.pool import ThreadedConnectionPool

params = {
    "user": "postgres",
    "password": "postgres",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "postgres"
}

pool = ThreadedConnectionPool(minconn=5, maxconn=20, **params)
with pool.getconn() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(version)