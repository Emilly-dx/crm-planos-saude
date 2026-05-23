from flask import Blueprint, request, redirect, url_for
from models.cobranca import salvar_cobranca

cobrancas_bp = Blueprint('cobrancas', __name__)

@cobrancas_bp.route("/cobrancas", methods=["POST"])
def cadastrar_cobranca():
    try:
        salvar_cobranca(request.form)
        return redirect(url_for('main.home'))
    except Exception as e:
        return f"Erro ao salvar cobrança: {e}"