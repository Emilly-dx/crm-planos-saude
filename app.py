from flask import Flask, request, render_template
from database.database import conectar

app = Flask(__name__)

# 🔹 ROTA PRINCIPAL (abre o sistema)
@app.route("/")
def home():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

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
        (nome, telefone, email, status, peso_kg, altura_cm, gravida, data_nascimento, rg, cpf)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            telefone,
            None,  # email (já que você não usa)
            status,
            peso,
            altura,
            gravida,
            data_nascimento,
            rg,
            cpf
    )

        cursor.execute(sql, valores)
        conn.commit()

        from flask import redirect, url_for

        return redirect(url_for('home'))

    except Exception as e:
        return f"Erro: {e}"

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)