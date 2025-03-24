import os

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DATA_PATH = os.path.join(os.path.dirname(__file__), 'app', 'data', 'stars.csv')
