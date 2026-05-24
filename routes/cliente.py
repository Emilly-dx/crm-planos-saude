from flask import Blueprint, request, redirect, url_for
from models.clientes import listar_todos_clientes, salvar_novo_cliente, atualizar_cliente, excluir_cliente
from models.alertas import criar_alerta

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    try:
        id_cliente = salvar_novo_cliente(request.form)
        data_retorno = request.form.get("data_retorno")
        if data_retorno:
            criar_alerta(id_cliente, data_retorno)
        return redirect(url_for('main.home'))
    except Exception as e:
        return f"Erro ao processar cadastro: {e}"

@clientes_bp.route("/clientes/<int:id>", methods=["POST"])
def editar_cliente(id):
    try:
        atualizar_cliente(id, request.form)
        return redirect(url_for('main.home'))
    except Exception as e:
        return f"Erro ao editar cliente: {e}"

@clientes_bp.route("/clientes/<int:id>/excluir", methods=["POST"])
def deletar_cliente(id):
    try:
        excluir_cliente(id)
        return redirect(url_for('main.home'))
    except Exception as e:
        return f"Erro ao excluir cliente: {e}"