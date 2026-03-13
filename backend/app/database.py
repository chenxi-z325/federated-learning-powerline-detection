import sqlite3

class Database:
    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS training_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            epoch INTEGER,
            accuracy REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS client_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id TEXT,
            training_time REAL,
            accuracy REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS global_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            round INTEGER,
            average_accuracy REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')

        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    db = Database()
    db.create_tables()
    db.close()