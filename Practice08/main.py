import psycopg2
from config import load_config 

def connect():
    """ Устанавливает соединение с сервером PostgreSQL """
    config = load_config()
    try:
        # Распаковка словаря с конфигами через **
        conn = psycopg2.connect(**config)
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка подключения: {error}")
        return None

def setup_database():
    """ Создает таблицу, если она еще не существует """
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

def search_contacts():
    pattern = input("Введите имя или номер для поиска: ")
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            # Вызов функции, которую мы создали в SQL
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            for row in rows:
                print(f"Имя: {row[0]}, Телефон: {row[1]}")
        conn.close()

def upsert_contact():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            # Вызов процедуры, которую мы создали в SQL
            cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
            conn.commit()
            print("Контакт обработан (Добавлен или Обновлен).")
        conn.close()

def main():
    setup_database()
    while True:
        print("\n--- Телефонная книга (Practice 8) ---")
        print("1. Поиск по шаблону")
        print("2. Добавить/Обновить контакт (Upsert)")
        print("3. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1': search_contacts()
        elif choice == '2': upsert_contact()
        elif choice == '3': break
        else: print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()  