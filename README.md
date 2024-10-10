# Отчёт по клиентам с кредитами

Этот проект предназначен для генерации отчёта клиентов с кредитными счетами, где баланс превышает 1000. Отчёт сохраняется в формате CSV.

## Структура проекта

- `main.py` — основной файл для генерации отчёта.
- `create_tables.py` — скрипт для создания таблиц и заполнения базы данных начальными данными.
- `config.py` — файл конфигурации для подключения к базе данных.
- `tests/` — директория с тестами.
  - `test_main.py` — тесты для проверки работы функции генерации отчёта.

## Требования

Перед запуском проекта, убедитесь, что установлены следующие зависимости:

- Python 3.10 или выше
- PostgreSQL
- Модули Python, указанные в `requirements.txt`

## Установка

1. Клонируйте проект:
    ```
    git clone <URL-репозитория>
    cd your_project
    ```

2. Создайте виртуальное окружение и активируйте его:

   - На **Linux/MacOS**:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

   - На **Windows**:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```

3. Установите зависимости:

    ```
    pip install -r requirements.txt
    ```

4. Настройте параметры базы данных в файле `.env`. Пример содержимого `.env`:

    ```
    DB_NAME=your_dbname
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ```

## Инициализация базы данных

1. Подключитесь к PostgreSQL и создайте базу данных и пользователя:

    ```
    sudo -i -u postgres
    psql
    CREATE DATABASE testdb;
    CREATE USER myuser WITH PASSWORD 'mypassword';
    GRANT ALL PRIVILEGES ON DATABASE testdb TO myuser;
    ```

2. Запустите скрипт для создания таблиц и вставки данных:

    ```
    python create_tables.py
    ```

## Запуск программы

Чтобы сгенерировать отчёт в формате CSV, выполните команду:

```
python main.py
```

## Для запуска тестов выполните команду:

```
python -m unittest discover -s tests
```
Тесты создадут временные файлы отчётов с префиксом test_report_, которые будут автоматически удалены после завершения.