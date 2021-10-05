import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://mouz:1234@restflask_db:5432/restflask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


URL_WEB = os.getenv("URL_WEB", "https://0ead-37-45-209-99.ngrok.io")
TELEGRAM_URL = "https://api.telegram.org"
