from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
USER_MANAGER_SECRET_KEY = os.environ.get("USER_MANAGER_SECRET_KEY")