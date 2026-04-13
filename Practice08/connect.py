import psycopg2
from config import load_config  # Assumes config.py has a load_config function

def connect():
    """ Connect to the PostgreSQL database server """
    config = load_config()
    try:
        # Establish the connection using parameters from config.py
        with psycopg2.connect(**config) as conn:
            print('Successfully connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        # Handles connection and authentication errors mentioned in troubleshooting [5]
        print(f"Error while connecting to PostgreSQL: {error}")
        return None

if __name__ == '__main__':
    connect()