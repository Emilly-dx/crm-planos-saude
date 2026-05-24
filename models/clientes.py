from database.database import conectar

def listar_todos_clientes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

def salvar_novo_cliente(dados):
    conn = conectar()
    cursor = conn.cursor()
    
    gravida = 1 if dados.get("gravida") == "sim" else 0
    
    # Converte vírgula para ponto nos campos decimais
    peso = dados.get("peso_kg", "").replace(",", ".") or None
    altura = dados.get("altura_cm", "").replace(",", ".") or None

    sql = """
    INSERT INTO clientes 
    (nome, telefone, email, status, peso_kg, altura_cm, gravida, data_nascimento, rg, cpf)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    valores = (
        dados.get("nome"),
        dados.get("telefone"),
        dados.get("email"),
        dados.get("status"),
        peso,
        altura,
        gravida,
        dados.get("data_nascimento"),
        dados.get("rg"),
        dados.get("cpf")
    )

    cursor.execute(sql, valores)
    novo_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return novo_id

def atualizar_cliente(id, dados):
    conn = conectar()
    cursor = conn.cursor()
    gravida = 1 if dados.get("gravida") == "sim" else 0

    # Converte vírgula para ponto nos campos decimais
    peso = dados.get("peso_kg", "").replace(",", ".") or None
    altura = dados.get("altura_cm", "").replace(",", ".") or None

    sql = """
    UPDATE clientes SET
        nome = %s,
        telefone = %s,
        email = %s,
        status = %s,
        peso_kg = %s,
        altura_cm = %s,
        gravida = %s,
        data_nascimento = %s,
        rg = %s,
        cpf = %s
    WHERE id = %s
    """
    valores = (
        dados.get("nome"),
        dados.get("telefone"),
        dados.get("email"),
        dados.get("status"),
        peso,
        altura,
        gravida,
        dados.get("data_nascimento"),
        dados.get("rg"),
        dados.get("cpf"),
        id
    )
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()

def excluir_cliente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alertas WHERE cliente_id = %s", (id,))
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()