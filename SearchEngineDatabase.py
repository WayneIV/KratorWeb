import sqlite3

class KratorSearchEngine:
    def __init__(self, db_path='search_engine.db'):
        self.db_path = db_path
        self.initialize_db()

    def initialize_db(self):
        # Connect to the SQLite database
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        # Create the 'pages' table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS pages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def search(self, query):
        # Connect to the SQLite database
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        # Perform the search using SQL query
        c.execute("SELECT url, content FROM pages WHERE content LIKE ?", ('%' + query + '%',))
        results = c.fetchall()

        # Close the connection
        conn.close()

        return results
