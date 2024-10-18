import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextBrowser
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QAction
import os
from flask import Flask, render_template, send_from_directory
import os

# Create the Flask application
app = Flask(__name__, static_url_path='/static')

# Route to serve the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve static files (CSS, JS, fonts, etc.)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), path)

# Start the Flask web server
if __name__ == '__main__':
    app.run(debug=True)


class KratorWeb(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KratorWeb")
        self.setGeometry(100, 100, 1024, 768)

        # Set up the UI
        self.setup_ui()

    def setup_ui(self):
        """Setup the main UI layout and load assets."""
        layout = QVBoxLayout()

        # Search bar for the custom search engine
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter search query...")
        layout.addWidget(self.search_input)

        # Search button with an icon
        self.search_button = QPushButton("Search", self)
        self.search_button.setIcon(QIcon(os.path.join('assets', 'images', 'search-icon.png')))
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)

        # Text area to display search results
        self.search_results = QTextBrowser(self)
        layout.addWidget(self.search_results)

        # Web view for displaying pages
        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)

        # Set up a container widget and apply layout
        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Load styles from CSS
        self.load_stylesheet()

        # Load custom fonts
        self.load_custom_fonts()

    def perform_search(self):
        """Perform a search (dummy function for now)."""
        query = self.search_input.text()
        if query:
            self.search_results.setPlainText(f"Search for: {query}")

    def load_stylesheet(self):
        """Load and apply custom CSS from the assets folder."""
        css_path = os.path.join('assets', 'css', 'style.css')
        if os.path.exists(css_path):
            with open(css_path, 'r') as f:
                stylesheet = f.read()
                self.setStyleSheet(stylesheet)
        else:
            print("CSS file not found!")

    def load_custom_fonts(self):
        """Load and apply custom fonts from the assets/fonts folder."""
        font_path = os.path.join('assets', 'fonts', 'custom-font.ttf')
        if os.path.exists(font_path):
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id != -1:
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                font = QFont(font_family)
                self.setFont(font)
            else:
                print("Font could not be loaded.")
        else:
            print("Font file not found.")

if __name__ == '__main__':
    # Initialize the application
    app = QApplication(sys.argv)

    # Create and show the browser window
    window = KratorWeb()
    window.show()

    # Run the application event loop
    sys.exit(app.exec_())
