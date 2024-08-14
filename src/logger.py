import sqlite3

class Logger:
    def __init__(self, db_name='../data/social_media_logs.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            platform TEXT,
            summary TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log(self, platform, summary):
        query = "INSERT INTO logs (platform, summary) VALUES (?, ?)"
        self.conn.execute(query, (platform, summary))
        self.conn.commit()

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.log("Twitter", "This is a test summary!")
