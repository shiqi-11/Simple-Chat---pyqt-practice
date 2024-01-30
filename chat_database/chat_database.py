import sqlite3


def init_db():
    conn = sqlite3.connect('chathistory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      sender TEXT,
                      message TEXT,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
