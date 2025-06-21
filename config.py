from dotenv import load_dotenv
import os

# Charger le fichier .env automatiquement
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_clef_secrete_pour_le_dev'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Mail (config exemple, adapte avec ton SMTP)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # mettre email
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # mettre mdp
MAIL_DEFAULT_SENDER = MAIL_USERNAME
