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
    
    # 1. Pegamos os dados vindo do HTML (atributo 'name')
    # 2. Tratamos o campo grávida (sim vira 1, qualquer outra coisa vira 0)
    gravida = 1 if dados.get("gravida") == "sim" else 0
    
    # SQL com os nomes REAIS das suas colunas no MySQL
    sql = """
    INSERT INTO clientes 
    (nome, telefone, email, status, peso_kg, altura_cm, gravida, data_nascimento, rg, cpf)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Valores organizados para o INSERT
    valores = (
        dados.get("nome"),
        dados.get("telefone"),
        dados.get("email"), # Caso tenha esse campo no form, senão mande None
        dados.get("status"),
        dados.get("peso_kg"),
        dados.get("altura_cm"),
        gravida,
        dados.get("data_nascimento"),
        dados.get("rg"),
        dados.get("cpf")
    )

    cursor.execute(sql, valores)
    novo_id = cursor.lastrowid #pega o ID gerado
    conn.commit()
    cursor.close()
    conn.close()
    return novo_id #devolve o ID

def atualizar_cliente(id, dados):
    conn = conectar()
    cursor = conn.cursor()
    gravida = 1 if dados.get("gravida") == "sim" else 0
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
        dados.get("peso_kg"),
        dados.get("altura_cm"),
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
    # Exclui alertas vinculados primeiro (evita erro de chave estrangeira)
    cursor.execute("DELETE FROM alertas WHERE cliente_id = %s", (id,))
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
