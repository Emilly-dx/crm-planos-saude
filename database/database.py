import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "crm_saude")
        )
    except mysql.connector.Error as err:
        print(f"Erro no MySQL: {err}")
        return None