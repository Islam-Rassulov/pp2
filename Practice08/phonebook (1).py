import psycopg2
from config import load_config 

def setup_database():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        name VARCHAR(100) PRIMARY KEY,
        phone VARCHAR(20) NOT NULL
    );
    """
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(create_table_query)
                conn.commit()
                print("Проверка базы данных: Таблица 'contacts' готова к работе.")
        except Exception as e:
            print(f"Ошибка при инициализации таблицы: {e}")
        finally:
            conn.close()

def connect():
    """ Connect to the PostgreSQL database server """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        return None

def search_contacts():
    pattern = input("Enter name or phone pattern to search: ")
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
            rows = cur.fetchall()
            for row in rows:
                print(f"Name: {row[0]}, Phone: {row[1]}")
        conn.close()

def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
            conn.commit()
            print("Contact processed (Inserted or Updated).")
        conn.close()

def bulk_insert():
    # Example logic for bulk insert task [2]
    data = []
    print("Enter contacts (name,phone). Type 'done' to finish:")
    while True:
        entry = input("> ")
        if entry.lower() == 'done': break
        if ',' in entry:
            data.append(tuple(entry.split(',')))
    
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            names = [d[0] for d in data]
            phones = [d[1] for d in data]
            cur.execute("CALL bulk_insert_contacts(%s, %s);", (names, phones))
            conn.commit()
            print("Bulk insert completed.")
        conn.close()

def get_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
            for row in cur.fetchall():
                print(row)
        conn.close()

def delete_contact():
    identifier = input("Enter name or phone to delete: ")
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact_by_identity(%s);", (identifier,))
            conn.commit()
            print("Delete operation executed.")
        conn.close()

def main():
    setup_database()
    while True:
        print("\n--- PhoneBook Practice 8 ---")
        print("1. Search (Pattern)")
        print("2. Add/Update Contact (Upsert)")
        print("3. Bulk Insert")
        print("4. View Paginated")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choice: ")
        
        if choice == '1': search_contacts()
        elif choice == '2': upsert_contact()
        elif choice == '3': bulk_insert()
        elif choice == '4': get_paginated()
        elif choice == '5': delete_contact()
        elif choice == '6': break

if __name__ == "__main__":
    main()