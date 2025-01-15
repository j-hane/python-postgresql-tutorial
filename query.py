import psycopg2
import json
from decimal import Decimal
from datetime import datetime

def custom_serializer(obj):
    """Custom serializer for non-serializable types."""
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 string
    raise TypeError(f"Type {type(obj)} not serializable")

def fetch_data_from_table(table_name):
    """Fetch data from the specified table and return it as JSON."""
    try:
        # Use context manager for connection
        with psycopg2.connect(
            host="localhost",
            database="testdb",
            user="postgres",
            password="password"
        ) as connection:
            # Use context manager for cursor
            with connection.cursor() as cursor:
                # Execute the query
                select_query = f"SELECT * FROM {table_name};"
                cursor.execute(select_query)
                
                # Fetch column names
                col_names = [desc[0] for desc in cursor.description]
                
                # Fetch all rows
                rows = cursor.fetchall()
                
                # Convert rows to a list of dictionaries
                results = [dict(zip(col_names, row)) for row in rows]
                
                # Return JSON representation
                return json.dumps(results, indent=4, default=custom_serializer)

    except psycopg2.Error as db_error:
        return json.dumps({"error": f"Database error: {db_error}"}, indent=4)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

if __name__ == "__main__":
    # Replace 'employees' with your table name
    table_name = "employees"
    print(fetch_data_from_table(table_name))