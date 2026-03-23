from flask import Flask, jsonify, request
from database.database import conectar

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend funcionando!"

@app.route("/teste-banco")
def teste_banco():
    try:
        conn = conectar()
        return "Conectado ao banco com sucesso!"
    except Exception as e:
        return f"Erro: {e}"
    finally:
        conn.close()

@app.route("/clientes")
def listar_clientes():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clientes")
        dados = cursor.fetchall()

        return jsonify(dados)  # agora retorna JSON

    except Exception as e:
        return f"Erro: {e}"

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    try:
        # Pegando dados do formulário
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        status = request.form.get("status")

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO clientes (nome, telefone, email, status)
        VALUES (%s, %s, %s, %s)
        """

        valores = (nome, telefone, email, status)

        cursor.execute(sql, valores)
        conn.commit()

        return "Cliente cadastrado com sucesso!"

    except Exception as e:
        return f"Erro: {e}"

    finally:
        cursor.close()
        conn.close()