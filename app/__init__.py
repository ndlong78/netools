from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from app.app import index, results
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/results', 'results', results)

    return app