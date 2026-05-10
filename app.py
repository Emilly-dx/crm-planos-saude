from flask import Flask, request, render_template, redirect, url_for
from models.clientes import listar_todos_clientes, salvar_novo_cliente
from models.alertas import criar_alerta, listar_alertas_pendentes, contar_alertas_hoje

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def home():
    clientes = listar_todos_clientes()
    alertas = listar_alertas_pendentes()
    total_hoje = contar_alertas_hoje()
    
    return render_template("Plano.html", 
                           clientes=clientes, 
                           alertas=alertas, 
                           total_hoje=total_hoje)

@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    try:
        # 1. Salva o cliente e recebe o ID dele de volta
        id_cliente = salvar_novo_cliente(request.form)
        
        # 2. Pega a data de retorno do formulário e cria o alerta
        data_retorno = request.form.get("data_retorno")
        if data_retorno:
            criar_alerta(id_cliente, data_retorno)
            
        return redirect(url_for('home'))
    except Exception as e:
        return f"Erro ao processar cadastro: {e}"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)