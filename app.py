from flask import Flask, request, render_template
from database.database import conectar

app = Flask(__name__)

# 🔹 ROTA PRINCIPAL (abre o sistema)
@app.route("/")
def home():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("Plano.html", clientes=clientes)

# 🔹 CADASTRAR CLIENTE
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    try:
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")

        gravida = request.form.get("gravida")
        # Converter para 0 ou 1
        if gravida == "sim":
            gravida = 1
        else:
            gravida = 0
        
        rg = request.form.get("rg")
        cpf = request.form.get("cpf")
        data_nascimento = request.form.get("data_nascimento")
        altura = request.form.get("altura_cm")
        peso = request.form.get("peso_kg")
        status = request.form.get("status")

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO clientes 
        (nome, telefone, gravida, rg, cpf, data_nascimento, altura_cm, peso_kg, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (nome, telefone, gravida, rg, cpf, data_nascimento, altura, peso, status)

        cursor.execute(sql, valores)
        conn.commit()

        return "Cliente cadastrado com sucesso!"

    except Exception as e:
        return f"Erro: {e}"

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)