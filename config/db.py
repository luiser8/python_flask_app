from app import app
from psycopg2 import connect, sql
from dotenv import load_dotenv
import os

load_dotenv()

# POSTGRESQL Connection
url = os.getenv("DB")
pgsqlConn = connect(url)
