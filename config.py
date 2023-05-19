import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    _true_values = ['yes', 'y', 'true', '1']
    FLASK_HOST = os.getenv("FLASK_HOST")
    FLASK_PORT = os.getenv("FLASK_PORT")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG").lower() in _true_values
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
