from flask import Flask

app = Flask(__name__)

from app import app  # Import the app module to ensure routes are registered