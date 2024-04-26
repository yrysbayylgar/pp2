import psycopg2
import csv

def setup_database():
    """Establishes a connection to the PostgreSQL database and creates necessary tables."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phone_directory (
            entry_id SERIAL PRIMARY KEY,
            first_name VARCHAR(32) NOT NULL,
            surname VARCHAR(32) NOT NULL,
            phone_number VARCHAR(11) NOT NULL
        )
        """,
    )
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as connection:
            with connection.cursor() as cursor:
                for command in commands:
                    cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def add_entry():
    """Adds a new entry to the phone directory."""
    data = (input("Enter first name: "), input("Enter surname: "), input("Enter phone number: "))
    command = """
        INSERT INTO phone_directory(first_name, surname, phone_number) 
        VALUES(%s, %s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as connection:
            with connection.cursor() as cursor:
                cursor.execute(command, data)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def import_from_csv():
    """Imports data from a CSV file into the phone directory."""
    command = """
        INSERT INTO phone_directory(first_name, surname, phone_number) 
        VALUES(%s, %s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as connection:
            with connection.cursor() as cursor:
                with open('numbers.csv', 'r', newline='') as file:
                    rows = csv.reader(file)
                    
                    for data in rows:
                        cursor.execute(command, (data[0], data[1], data[2]))

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def remove_entry():
    """Removes an entry from the phone directory based on the first name."""
    name = input("Enter the first name: ")
    
    command = """
        DELETE FROM phone_directory 
        WHERE first_name = %s;
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as connection:
            with connection.cursor() as cursor:
                cursor.execute(command, (name,))
                print(f"Number of entries deleted: {cursor.rowcount}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def display_entries(order_by_id: bool):
    """Displays entries in the phone directory, optionally ordered by ID."""
    if order_by_id:
        command = """
            SELECT entry_id, first_name, surname, phone_number FROM phone_directory ORDER BY entry_id;
        """
    else:
        command = """
            SELECT entry_id, first_name, surname, phone_number FROM phone_directory ORDER BY first_name;
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as connection:
            with connection.cursor() as cursor:
                cursor.execute(command)
                print("-----------------------------------------------------")
                for data in cursor.fetchall():
                    print(f"| {data[0]} | {data[1]} | {data[2]} | {data[3]} |")
                
                print(f"Number of entries: {cursor.rowcount}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    setup_database()
    add_entry()
    import_from_csv()
    remove_entry()
    display_entries(True)
