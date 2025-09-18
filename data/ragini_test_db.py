import sqlite3

# Create (or connect to) the test database
conn = sqlite3.connect('data/test_buzz.sqlite')
cursor = conn.cursor()

# Create a table (customize as needed)
cursor.execute('''
CREATE TABLE IF NOT EXISTS streamed_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    category TEXT,
    sentiment REAL,
    user_id TEXT,
    message_text TEXT
)
''')

conn.commit()
conn.close()
print("Test database created: data/test_buzz.sqlite")