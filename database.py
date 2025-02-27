import sqlite3
import unicodedata

DB_NAME = 'quotes.db'

def normalize_key(key):
    normalized = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore').decode('utf-8')
    return normalized.lower().replace(' ', '_')

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table with searchable driver_key column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver TEXT NOT NULL,
            driver_key TEXT NOT NULL UNIQUE,
            quote TEXT NOT NULL
        )
    ''')

    # Sample quotes
    sample_quotes = [
        ("Sebastian Vettel","There's something loose between my legs. Apart from the obvious. Something is flying around my feet. I'd be proud if it was what you think it is, but it's not"),
        ("Kimi Räikkönen","Leave me alone, I know what I'm doing"),
        ("Nico Rosberg","I was faster than you today"),
        ("Fernando Alonso","GP2 engine, GP2 engine! Aaaargh!"),
        ("Jenson Button","I'm going to pee in your seat"),
        ("Lewis Hamilton","Still, I rise"),
        ("Daniel Ricciardo","I'm tripping major nuts")]

    # Insert data with normalized driver_key
    cursor.executemany("INSERT INTO quotes (driver, driver_key, quote) VALUES (?, ?, ?)", [(name, normalize_key(name), quote) for name, quote in sample_quotes])

    conn.commit()
    conn.close()
    print('Database initialized')

if __name__=='__main__':
    initialize_db()
