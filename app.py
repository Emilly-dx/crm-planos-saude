from flask import Flask, request, render_template, redirect, url_for, session, flash
from functools import wraps
from models.clientes import listar_todos_clientes, salvar_novo_cliente, atualizar_cliente, excluir_cliente
from models.alertas import criar_alerta, listar_alertas_pendentes, contar_alertas_hoje, atualizar_data_alerta
from models.negociacao import listar_negociacoes, salvar_negociacao, contar_negociacoes_abertas
from models.cobranca import listar_cobrancas, salvar_cobranca, contar_cobrancas_em_dia, contar_cobrancas_atrasadas
from models.corretores import verificar_login, atualizar_senha, buscar_corretor_por_email

app = Flask(__name__)
app.secret_key = "troque-por-algo-secreto-aqui"

# Protege rotas que exigem login
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("corretor_id"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("corretor_id"):
        return redirect(url_for("home"))
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")
        corretor = verificar_login(email, senha)
        if corretor:
            session["corretor_id"] = corretor["id"]
            session["corretor_nome"] = corretor["nome"]
            session["corretor_email"] = corretor["email"]
            return redirect(url_for("home"))
        else:
            flash("E-mail ou senha incorretos.", "erro")
            return redirect(url_for("login"))
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# Dashboard
@app.route("/")
@login_required
def home():
    clientes = listar_todos_clientes()
    alertas = listar_alertas_pendentes()
    total_hoje = contar_alertas_hoje()
    negociacoes = listar_negociacoes()
    cobrancas = listar_cobrancas()

    total_clientes = len(clientes)
    total_negociacoes_abertas = contar_negociacoes_abertas()
    total_cobrancas_em_dia = contar_cobrancas_em_dia()
    cobrancas_atrasadas = contar_cobrancas_atrasadas()

    return render_template("Plano.html",
                           clientes=clientes,
                           alertas=alertas,
                           total_hoje=total_hoje,
                           negociacoes=negociacoes,
                           cobrancas=cobrancas,
                           total_clientes=total_clientes,
                           total_negociacoes_abertas=total_negociacoes_abertas,
                           total_cobrancas_em_dia=total_cobrancas_em_dia,
                           cobrancas_atrasadas=cobrancas_atrasadas,
                           corretor_nome=session.get("corretor_nome"))

# Configurações
@app.route("/configuracoes")
@login_required
def configuracoes():
    return render_template("configuracoes.html",
                           corretor_nome=session.get("corretor_nome"),
                           corretor_email=session.get("corretor_email"))

# Alterar Senha
@app.route("/alterar-senha", methods=["POST"])
@login_required
def alterar_senha():
    senha_atual = request.form.get("senha_atual")
    nova_senha = request.form.get("nova_senha")
    confirmar = request.form.get("confirmar_senha")

    corretor = buscar_corretor_por_email(session.get("corretor_email"))

    if not verificar_login(corretor["email"], senha_atual):
        flash("Senha atual incorreta.", "erro")
        return redirect(url_for("configuracoes"))

    if nova_senha != confirmar:
        flash("As senhas não coincidem.", "erro")
        return redirect(url_for("configuracoes"))

    if len(nova_senha) < 6:
        flash("A nova senha precisa ter pelo menos 6 caracteres.", "erro")
        return redirect(url_for("configuracoes"))

    atualizar_senha(corretor["email"], nova_senha)
    flash("Senha alterada com sucesso!", "sucesso")
    return redirect(url_for("configuracoes"))

# Clientes
@app.route("/clientes", methods=["POST"])
@login_required
def cadastrar_cliente():
    try:
        id_cliente = salvar_novo_cliente(request.form)
        data_retorno = request.form.get("data_retorno")
        if data_retorno:
            criar_alerta(id_cliente, data_retorno)
        return redirect(url_for("home"))
    except Exception as e:
        return f"Erro ao processar cadastro: {e}"

@app.route("/clientes/<int:id>", methods=["POST"])
@login_required
def editar_cliente(id):
    try:
        atualizar_cliente(id, request.form)
        return redirect(url_for("home"))
    except Exception as e:
        return f"Erro ao editar cliente: {e}"

@app.route("/clientes/<int:id>/excluir", methods=["POST"])
@login_required
def deletar_cliente(id):
    try:
        excluir_cliente(id)
        return redirect(url_for("home"))
    except Exception as e:
        return f"Erro ao excluir cliente: {e}"

# Negociações
@app.route("/negociacoes", methods=["POST"])
@login_required
def cadastrar_negociacao():
    try:
        salvar_negociacao(request.form)
        return redirect(url_for("home"))
    except Exception as e:
        return f"Erro ao salvar negociação: {e}"

# Cobranças
@app.route("/cobrancas", methods=["POST"])
@login_required
def cadastrar_cobranca():
    try:
        salvar_cobranca(request.form)
        return redirect(url_for("home"))
    except Exception as e:
        return f"Erro ao salvar cobrança: {e}"
    
# Alertas
@app.route("/alertas/<int:id>/editar", methods=["POST"])
@login_required
def editar_alerta(id):
    try:
        nova_data = request.form.get("data_retorno")
        atualizar_data_alerta(id, nova_data)
        return redirect(url_for("home"))
    except Exception as e:
        return f"Erro ao editar alerta: {e}"

# Inicialização
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)