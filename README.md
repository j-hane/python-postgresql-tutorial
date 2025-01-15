
# Python with PostgreSQL Tutorial

This project demonstrates how to use Python to interact with a PostgreSQL database using the `psycopg2` library.

## Project Structure
- `insert_data.py`: Inserts sample data into the `employees` table.
- `query.py`: Fetches and displays data from the `employees` table.
- `requirements.txt`: Lists the Python dependencies.
- `sample_output.txt`: Contains example output from running the scripts.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/j-hane/python-postgresql-tutorial.git
   cd python-postgresql-tutorial
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set up your PostgreSQL database and update the scripts with your credentials.

## How to Run
1. Run the `insert_data.py` script to insert sample data:
   ```bash
   python insert_data.py
   ```

2. Run the `fetch_data.py` script to fetch and display the data:
   ```bash
   python fetch_data.py
   ```

## Sample Output
```
(1, 'Alice', 'Developer', 80000)
(2, 'Bob', 'Designer', 70000)
```
