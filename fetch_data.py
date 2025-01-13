
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="password"
    )
    cursor = connection.cursor()
    select_query = "SELECT * FROM employees;"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("Error:", e)
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
