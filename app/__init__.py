from flask import Flask
import sys
import os

def create_app():
    app = Flask(__name__)

    # Thêm thư mục 'app' vào đường dẫn Python
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))

    # Import routes
    from app.app import index, results, saved_results, tracert_progress
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/results', 'results', results)
    app.add_url_rule('/saved_results', 'saved_results', saved_results)
    app.add_url_rule('/tracert_progress/<host>', 'tracert_progress', tracert_progress)

    return app