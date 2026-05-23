from flask import Blueprint, request, redirect, url_for
from models.negociacao import salvar_negociacao

negociacoes_bp = Blueprint('negociacoes', __name__)

@negociacoes_bp.route("/negociacoes", methods=["POST"])
def cadastrar_negociacao():
    try:
        salvar_negociacao(request.form)
        return redirect(url_for('main.home'))
    except Exception as e:
        return f"Erro ao salvar negociação: {e}"