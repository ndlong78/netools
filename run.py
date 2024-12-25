import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(host='0.0.0.0', port=8000, debug=debug_mode)