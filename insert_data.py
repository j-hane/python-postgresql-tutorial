
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="password"
    )
    cursor = connection.cursor()
    insert_query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, ("Alice", "Developer", 80000))
    cursor.execute(insert_query, ("Bob", "Designer", 70000))
    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    print("Error:", e)
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
