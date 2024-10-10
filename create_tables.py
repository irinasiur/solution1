import psycopg2
from config import DB_CONFIG


def execute_sql_commands():
    create_tables = """
        CREATE TABLE IF NOT EXISTS CLIENT (
            id SERIAL PRIMARY KEY,
            "First Name" VARCHAR(100),
            "Last Name" VARCHAR(100),
            "Middle Name" VARCHAR(100)
        );

        CREATE TABLE IF NOT EXISTS CREDIT (
            id SERIAL PRIMARY KEY,
            "Credit Number" VARCHAR(20),
            Amount NUMERIC(12, 2),
            "Balance" NUMERIC(12, 2)
        );

        CREATE TABLE IF NOT EXISTS RELATION (
            id SERIAL PRIMARY KEY,
            "Client" INT REFERENCES CLIENT(id),
            "Credit" INT REFERENCES CREDIT(id)
        );
    """

    insert_data = """
        INSERT INTO CLIENT ("First Name", "Last Name", "Middle Name") VALUES
        ('Иван', 'Иванов', 'Иванович'),
        ('Петр', 'Петров', 'Петрович'),
        ('Мария', 'Сидорова', 'Александровна'),
        ('Сергей', 'Кузнецов', 'Васильевич'),
        ('Ольга', 'Смирнова', 'Николаевна');

        INSERT INTO CREDIT ("Credit Number", Amount, "Balance") VALUES
        ('1234567890', 5000, 1500),
        ('0987654321', 3000, 500),
        ('1111222233', 7000, 2000),
        ('4444555566', 10000, 1200),
        ('7777888899', 4500, 300);

        INSERT INTO RELATION ("Client", "Credit") VALUES
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5);
    """

    try:
        conn = psycopg2.connect(
            dbname=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor()

        cursor.execute(create_tables)
        conn.commit()

        cursor.execute(insert_data)
        conn.commit()

        print("Таблицы созданы и данные успешно добавлены!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    execute_sql_commands()
