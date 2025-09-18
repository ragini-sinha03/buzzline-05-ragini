
import json
import sqlite3
import pathlib

DATA_FILE = pathlib.Path('data/project_live.json')
DB_FILE = pathlib.Path('data/ragini_processed.sqlite')

def init_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS message_insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            sentiment REAL
        )
    ''')
    conn.commit()
    conn.close()

def store_insight(message, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO message_insights (category, sentiment)
        VALUES (?, ?)
    ''', (
        message.get("category"),
        message.get("sentiment")
    ))
    conn.commit()
    conn.close()

def read_one_message(data_file):
    with open(data_file, 'r') as f:
        for line in f:
            if line.strip():
                message = json.loads(line.strip())
                return message  # Only process the first available message

def main():
    init_db(DB_FILE)
    print(f"Reading one message from {DATA_FILE} and storing category and sentiment in {DB_FILE}")
    message = read_one_message(DATA_FILE)
    if message:
        store_insight(message, DB_FILE)
        print("Processed and stored one message insight.")
    else:
        print("No message found.")

if __name__ == "__main__":
    main()