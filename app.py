from flask import Flask, request, render_template, redirect, url_for, jsonify
from models.clientes import listar_todos_clientes, salvar_novo_cliente, atualizar_cliente, excluir_cliente
from models.alertas import criar_alerta, listar_alertas_pendentes, contar_alertas_hoje

app = Flask(__name__)

@app.route("/")
def home():
    clientes = listar_todos_clientes()
    alertas = listar_alertas_pendentes()
    total_hoje = contar_alertas_hoje()
    return render_template("Plano.html", clientes=clientes, alertas=alertas, total_hoje=total_hoje)

@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    try:
        id_cliente = salvar_novo_cliente(request.form)
        data_retorno = request.form.get("data_retorno")
        if data_retorno:
            criar_alerta(id_cliente, data_retorno)
        return redirect(url_for('home'))
    except Exception as e:
        return f"Erro ao processar cadastro: {e}"

@app.route("/clientes/<int:id>", methods=["POST"])
def editar_cliente(id):
    try:
        atualizar_cliente(id, request.form)
        return redirect(url_for('home'))
    except Exception as e:
        return f"Erro ao editar cliente: {e}"

@app.route("/clientes/<int:id>/excluir", methods=["POST"])
def deletar_cliente(id):
    try:
        excluir_cliente(id)
        return redirect(url_for('home'))
    except Exception as e:
        return f"Erro ao excluir cliente: {e}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)