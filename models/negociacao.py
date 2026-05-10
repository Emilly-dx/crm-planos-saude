from database.database import conectar

def inserir_negociacao(cliente_id, plano, valor, status, data):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO negociacoes 
    (cliente_id, plano, valor, status, data)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (cliente_id, plano, valor, status, data)

    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()