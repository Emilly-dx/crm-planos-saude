from models.corretores import criar_corretor

nome  = "Edson"
email = "edsonfernandes.corretor64@gmail.com"
senha = "Planodesaude2026*"

sucesso = criar_corretor(nome, email, senha)

if sucesso:
    print(f"✅ Corretor '{nome}' criado com sucesso!")
else:
    print("❌ Erro ao criar corretor.")