import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")
PRO_USER = os.getenv("PRO_USER")
PRO_PASS = os.getenv("PRO_PASS")