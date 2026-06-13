from database.database import conectar

# função criar alerta
def criar_alerta(cliente_id, data_retorno):
    if not data_retorno:
        return 
        
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO alertas (cliente_id, data_retorno, descricao, status) VALUES (%s, %s, %s, %s)"
    valores = (cliente_id, data_retorno, "Retorno agendado pelo corretor", "Pendente")
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()

# função para mostrar na tela
def listar_alertas_pendentes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    sql = """
    SELECT a.id, c.nome, c.telefone, a.data_retorno, a.descricao, a.status 
    FROM alertas a
    JOIN clientes c ON a.cliente_id = c.id
    WHERE a.status = 'Pendente'
    ORDER BY a.data_retorno ASC
    """
    
    cursor.execute(sql)
    alertas = cursor.fetchall()
    cursor.close()
    conn.close()
    return alertas

def contar_alertas_hoje():
    conn = conectar()
    cursor = conn.cursor()
    # CURDATE() é uma função do MySQL que pega a data de hoje
    sql = "SELECT COUNT(*) FROM alertas WHERE data_retorno = CURDATE() AND status = 'Pendente'"
    cursor.execute(sql)
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total

def atualizar_data_alerta(id, nova_data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE alertas SET data_retorno = %s WHERE id = %s", (nova_data, id))
    conn.commit()
    cursor.close()
    conn.close()

def excluir_alerta(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alertas WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def excluir_alertas_vencidos():
    from datetime import date
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alertas WHERE data_retorno < %s", (date.today(),))
    conn.commit()
    cursor.close()
    conn.close()
