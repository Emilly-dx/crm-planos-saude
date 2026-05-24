from database.database import conectar
from werkzeug.security import generate_password_hash, check_password_hash

def buscar_corretor_por_email(email):
    conn = conectar()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM corretores WHERE email = %s", (email,))
    corretor = cursor.fetchone()
    cursor.close()
    conn.close()
    return corretor

def verificar_login(email, senha):
    corretor = buscar_corretor_por_email(email)
    if not corretor:
        return None
    if check_password_hash(corretor["senha_hash"], senha):
        return corretor
    return None

def criar_corretor(nome, email, senha):
    conn = conectar()
    if not conn:
        return False
    cursor = conn.cursor()
    senha_hash = generate_password_hash(senha)
    try:
        cursor.execute(
            "INSERT INTO corretores (nome, email, senha_hash) VALUES (%s, %s, %s)",
            (nome, email, senha_hash)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar corretor: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        
def atualizar_senha(email, nova_senha):
    conn = conectar()
    if not conn:
        return False
    cursor = conn.cursor()
    senha_hash = generate_password_hash(nova_senha)
    cursor.execute(
        "UPDATE corretores SET senha_hash = %s WHERE email = %s",
        (senha_hash, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True