from database.database import conectar

def listar_negociacoes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    sql = """
    SELECT n.id, c.nome, n.plano, n.valor, n.data, n.status
    FROM negociacoes n
    JOIN clientes c ON n.cliente_id = c.id
    ORDER BY n.data DESC
    """
    cursor.execute(sql)
    negociacoes = cursor.fetchall()
    cursor.close()
    conn.close()
    return negociacoes

def salvar_negociacao(form):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO negociacoes 
             (cliente_id, plano, valor, data, status) 
             VALUES (%s, %s, %s, %s, %s)"""
    valores = (
        form.get("cliente_id"),
        form.get("plano"),
        form.get("valor"),
        form.get("data"),
        form.get("status")
    )
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()