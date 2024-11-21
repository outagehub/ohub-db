import sqlite3
import os

# Path to your SQLite database file
DB_FILE = "ohub-db/outages_db"

# Ensure the directory exists
os.makedirs("ohub-db", exist_ok=True)

def initialize_database():
    """Create the database and table if they don't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Define the outages table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS outages (
            id TEXT PRIMARY KEY,
            municipality TEXT,
            area TEXT,
            cause TEXT,
            numCustomersOut INTEGER,
            crewStatusDescription TEXT,
            latitude REAL,
            longitude REAL,
            dateOff TEXT,
            crewEta TEXT,
            polygon TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_FILE}")

if __name__ == "__main__":
    initialize_database()


