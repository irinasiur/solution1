import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import csv
import os
from main import generate_report


class TestClientCreditReport(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_query_execution(self, mock_connect):
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            ('Иван Иванов', '1234567890'),
            ('Мария Сидорова', '1111222233'),
            ('Сергей Кузнецов', '4444555566')
        ]
        mock_connect.return_value = mock_conn

        current_date = datetime.now().strftime("%d.%m.%Y")
        file_name = f"test_report_{current_date}.csv"

        generate_report(file_name)

        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once()
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            self.assertEqual(rows[0], ['Client Name', 'Credit Number'])
            self.assertEqual(rows[1], ['Иван Иванов', '1234567890'])
            self.assertEqual(rows[2], ['Мария Сидорова', '1111222233'])
            self.assertEqual(rows[3], ['Сергей Кузнецов', '4444555566'])

        os.remove(file_name)

    @patch('psycopg2.connect')
    def test_empty_result(self, mock_connect):
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = []
        mock_connect.return_value = mock_conn

        current_date = datetime.now().strftime("%d.%m.%Y")
        file_name = f"test_report_{current_date}.csv"

        generate_report(file_name)

        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once()
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            self.assertEqual(rows[0], ['Client Name', 'Credit Number'])
            self.assertEqual(len(rows), 1)

        os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
