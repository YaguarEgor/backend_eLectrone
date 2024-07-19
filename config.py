from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
NAME = os.environ.get("NAME")
USER = os.environ.get("USER")
PASS = os.environ.get("PASS")
SECRET_COOKIE = os.environ.get("SECRET_COOKIE")
SECRET_MANAGER = os.environ.get("SECRET_MANAGER")
