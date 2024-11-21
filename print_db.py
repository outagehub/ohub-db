import sqlite3

# Path to your SQLite database
DB_FILE = "ohub-db/outages_db"

def print_database():
    """Fetch and print all records from the outages table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Fetch all records
    cursor.execute("SELECT * FROM outages")
    records = cursor.fetchall()

    # Print records
    if records:
        for row in records:
            print(row)
    else:
        print("No records found in the outages table.")
    
    conn.close()

if __name__ == "__main__":
    print_database()


