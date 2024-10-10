import psycopg2
from config import DB_CONFIG
import csv
from datetime import datetime


def generate_report(file_name=None):
    if file_name is None:
        current_date = datetime.now().strftime("%d.%m.%Y")
        file_name = f"report_{current_date}.csv"

    conn = psycopg2.connect(
        dbname=DB_CONFIG['dbname'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port']
    )

    query = """
        SELECT
            c."First Name" || ' ' || c."Last Name" AS client_name,
            cr."Credit Number"
        FROM
            CLIENT c
        JOIN
            RELATION r ON c.id = r."Client"
        JOIN
            CREDIT cr ON cr.id = r."Credit"
        WHERE
            cr."Balance" > 1000
    """

    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Client Name", "Credit Number"])
        writer.writerows(data)

    print(f"Отчет успешно сохранен в файл {file_name}")


if __name__ == '__main__':
    generate_report()
