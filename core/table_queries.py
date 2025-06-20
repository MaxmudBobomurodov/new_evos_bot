from core.database_settings import execute_query

users = """
        CREATE TABLE IF NOT EXISTS users
        (
            id           SERIAL PRIMARY KEY,
            full_name    VARCHAR(64) NOT NULL,
            phone_number VARCHAR(15) NOT NULL UNIQUE,
            latitude     VARCHAR(20),
            longitude    VARCHAR(20),
            language     CHAR(2),
            chat_id      BIGINT,
            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """


def initializing_tables():
    execute_query(query=users)
