import psycopg2
from config import load_config
def create_tables():
    scripts = (
        """
        CREATE TABLE data_tiki (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            url_key VARCHAR(255) NOT NULL,
            price FLOAT NOT NULL,
            description VARCHAR(255),
            thumbnail_url VARCHAR(255) NOT NULL
        )
        """,
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for script in scripts:
                    cur.execute(script)
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    create_tables()