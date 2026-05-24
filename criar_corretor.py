from models.corretores import criar_corretor

nome  = "Seu Nome"
email = "seuemail@email.com"
senha = "SuaSenhaForte123!"

sucesso = criar_corretor(nome, email, senha)

if sucesso:
    print(f"✅ Corretor '{nome}' criado com sucesso!")
else:
    print("❌ Erro ao criar corretor.")