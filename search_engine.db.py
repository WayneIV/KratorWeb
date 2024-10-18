import sqlite3

class SearchEngineDB:
    def __init__(self, db_path='search_engine.db'):
        self.db_path = db_path
        self.initialize_db()

    def initialize_db(self):
        """Initialize the database and create the pages table if it doesn't exist."""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()

            # Create 'pages' table if it doesn't exist
            c.execute('''
                CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')
            conn.commit()
            print("Database initialized and 'pages' table created (if not already exists).")
        except sqlite3.Error as e:
            print(f"Error initializing DB: {e}")
        finally:
            conn.close()

    def insert_page(self, url, content):
        """Insert a new page into the 'pages' table."""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()

            # Insert page into the table
            c.execute("INSERT INTO pages (url, content) VALUES (?, ?)", (url, content))
            conn.commit()
            print(f"Page inserted: {url}")
        except sqlite3.Error as e:
            print(f"Error inserting page: {e}")
        finally:
            conn.close()

    def search(self, query):
        """Search for pages containing the given query in their content."""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()

            # Perform a search in the 'content' column
            c.execute("SELECT url, content FROM pages WHERE content LIKE ?", ('%' + query + '%',))
            results = c.fetchall()

            return results
        except sqlite3.Error as e:
            print(f"Error during search: {e}")
        finally:
            conn.close()


if __name__ == '__main__':
    # Create or connect to the database
    db = SearchEngineDB()

    # Insert sample pages
    db.insert_page('http://example.com', 'This is a sample page with some content.')
    db.insert_page('http://another.com', 'This page has different content.')

    # Perform a search
    search_results = db.search('sample')
    print("Search results:")
    for result in search_results:
        print(f"URL: {result[0]}\nContent: {result[1]}")
