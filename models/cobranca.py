from database.database import conectar

def listar_cobrancas():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    sql = """
    SELECT cb.id, c.nome, cb.valor, cb.data_vencimento, cb.status
    FROM cobrancas cb
    JOIN clientes c ON cb.cliente_id = c.id
    ORDER BY cb.data_vencimento ASC
    """
    cursor.execute(sql)
    cobrancas = cursor.fetchall()
    cursor.close()
    conn.close()
    return cobrancas

def salvar_cobranca(form):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO cobrancas 
             (cliente_id, valor, data_vencimento, status) 
             VALUES (%s, %s, %s, %s)"""
    valores = (
        form.get("cliente_id"),
        form.get("valor"),
        form.get("data_vencimento"),
        form.get("status")
    )
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()