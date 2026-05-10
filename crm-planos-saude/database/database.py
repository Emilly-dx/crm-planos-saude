import mysql.connector

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="crm_saude"
        )
    except mysql.connector.Error as err:
        print(f"Erro no MySQL: {err}")
        return None
