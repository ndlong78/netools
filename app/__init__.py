from flask import Flask
import sys
import os

def create_app():
    app = Flask(__name__)

    # Thêm thư mục 'app' vào đường dẫn Python
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))

    # Import routes
    from app.app import index, results
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/results', 'results', results)

    return app