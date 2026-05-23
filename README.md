# CRM para Corretor de Planos de Saúde

## Proposta do Sistema

Este projeto tem como objetivo desenvolver um sistema CRM (Customer Relationship Management) voltado para um corretor autônomo de planos de saúde. A aplicação permite o gerenciamento eficiente de clientes, possibilitando o cadastro, visualização e organização de informações, facilitando o acompanhamento e atendimento dos mesmos.

## Objetivo

Construir um sistema web funcional que integre frontend, backend e banco de dados, aplicando conceitos de engenharia de software e diferentes paradigmas de programação.

## Equipe de Desenvolvimento

Emilly Karoline Cunha Fernandes – Líder do projeto  
Responsável pelo desenvolvimento do backend utilizando Flask, integração com o banco de dados MySQL, implementação das regras de negócio, além do contato direto com o cliente e levantamento de requisitos.

Thierry Hanry Ribeiro da Silva Cardoso – Vice-líder do projeto  
Responsável pelo desenvolvimento do frontend utilizando HTML e CSS, com foco na interface e experiência do usuário.

## Tecnologias Utilizadas
- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript

## Ferramentas
- Git
- GitHub
- Visual Studio Code
- ngrok (testes externos)

## Funcionalidades Implementadas

* Cadastro de clientes via formulário web
* Armazenamento persistente em banco de dados MySQL
* Listagem dinâmica de clientes na interface
* Integração completa entre frontend e backend
* Atualização automática da tabela após inserção de dados
* Autenticação real com email e senha (hash bcrypt via werkzeug)
* Sessão segura com Flask Session
* Proteção de rotas — acesso negado sem login
* Logout funcional
* Alteração de senha pelo próprio corretor
* Listagem, edição inline e exclusão de clientes
* Cadastro de negociações vinculadas a clientes
* Cadastro de cobranças com status (Pago, Pendente, Atrasado)
* Alertas de retorno agendados por cliente
* Dashboard com métricas: total de clientes, negociações abertas, cobranças em dia e retornos do dia
* Armazenamento persistente em banco de dados MySQL
* Variáveis de ambiente via .env (segurança de credenciais)
* Interface responsiva com suporte mobile (menu drawer)


## Funcionalidades em Desenvolvimento

* Hospedagem na nuvem (Railway/Render)
* Recuperação de senha via email (Flask-Mail)
* Domínio personalizado
* Atualização na função mobile

## Arquitetura e Paradigmas Utilizados

O projeto integra diferentes paradigmas de programação:

### Programação Procedural

Utilizada na definição das rotas e funções do backend (Flask).

### A Programação Orientada a Objetos

Aplicada na modelagem das entidades do sistema, como Cliente e Cobrança. Permite encapsulamento de dados e comportamentos.

## Estrutura do Projeto

```
MVP_plano_saudes/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env                  (não versionado)
├── criar_corretor.py     (script de setup inicial)
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── models/
│   ├── __init__.py
│   ├── alertas.py
│   ├── clientes.py
│   ├── cobranca.py
│   ├── corretores.py
│   └── negociacao.py
│
├── routes/
│   ├── __init__.py
│   ├── cliente.py
│   ├── cobranca.py
│   └── negociacao.py
│
├── templates/
│   ├── login.html
│   └── Plano.html
│
├── static/
│   ├── Plano.css
│   └── js/
│       ├── login.js
│       └── meus_clientes.js
│
└── venv/                 (não versionado)

```

## Organização do Sistema

Durante o desenvolvimento do projeto, a estrutura da aplicação passou por diversas melhorias para facilitar a manutenção, escalabilidade e organização do código.

Inicialmente, grande parte da lógica do sistema estava concentrada no arquivo `app.py`. Com a evolução do projeto, foi realizada uma refatoração estrutural, separando as responsabilidades da aplicação em módulos específicos.

A pasta `models` foi criada para organizar as entidades do sistema, como clientes, negociações, cobranças, alertas e corretores, permitindo uma estrutura mais próxima dos conceitos de Programação Orientada a Objetos (POO).

Também foi implementada a pasta `routes`, responsável pela separação das rotas da aplicação em arquivos independentes, melhorando a organização do backend e facilitando futuras expansões do sistema.

Na camada de persistência de dados, foi criada a pasta `database`, responsável pela configuração e gerenciamento da conexão com o banco de dados MySQL.

No frontend, os arquivos HTML estão organizados na pasta `templates`, enquanto arquivos CSS e JavaScript estão separados na pasta `static`, seguindo a estrutura padrão utilizada pelo Flask.

Além disso, o projeto utiliza variáveis de ambiente através do arquivo `.env`, aumentando a segurança no armazenamento de credenciais sensíveis, como informações do banco de dados e chave secreta da aplicação.

Essa organização estrutural tornou o sistema mais modular, escalável e de fácil manutenção, permitindo maior facilidade na implementação de novas funcionalidades e correções futuras.


## Como Executar o Projeto

### 1. Clonar o repositório

bash
git clone https://github.com/Emilly-dx/crm-planos-saude.git


### 2. Acessar a pasta do projeto

bash
cd crm-planos-saude


### 3. Instalar as dependências

bash
pip install flask mysql-connector-python

bash
python -m venv venv
venv\Scripts\activate

### 4. Instalar dependências

bash
pip install -r requirements.txt

### 5. Configurar o arquivo .env
Crie um arquivo .env na raiz do projeto:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=crm_saude
SECRET_KEY=sua_chave_secreta


### 6. Configurar o banco de dados

Criar um banco no MySQL e executar:

sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100),
    status VARCHAR(50),
    peso_kg FLOAT,
    altura_cm FLOAT,
    gravida INT,
    data_nascimento DATE,
    rg VARCHAR(20),
    cpf VARCHAR(20)
);

### 7. Cadastrar o corretor

Edite o arquivo criar_corretor.py com nome, email e senha reais, depois execute:
python criar_corretor.py

### 8. Executar a aplicação

bash
python app.py


Acesse no navegador:


http://127.0.0.1:5000


## Roadmap do Projeto

### Etapa Atual

* Autenticação real com sessão Flask
* Proteção de rotas
* CRUD completo de clientes
* Módulo de negociações
* Módulo de cobranças
* Alertas de retorno
* Dashboard com métricas
* Alteração de senha
* Segurança com variáveis de ambiente


## Modelagem do Banco de Dados (Planejada)

O sistema utiliza o banco de dados MySQL para armazenamento persistente das informações, organizado através de tabelas relacionais responsáveis pelo gerenciamento das funcionalidades da aplicação.

Atualmente, o banco de dados é composto pelas seguintes entidades:

- Clientes
- Corretores
- Negociações
- Cobranças
- Alertas de retorno

A tabela `clientes` é responsável pelo armazenamento das informações principais dos clientes cadastrados no sistema, incluindo dados pessoais e informações utilizadas pelo corretor durante o atendimento.

A tabela `corretores` gerencia os usuários autenticados da aplicação, armazenando nome, email e senha criptografada utilizando hash de segurança.

As tabelas `negociacoes`, `cobrancas` e `alertas` possuem relacionamento com a tabela de clientes através de chaves estrangeiras, permitindo associar negociações, cobranças e retornos diretamente a cada cliente cadastrado.

Essa estrutura relacional permitiu maior organização dos dados, melhor integridade das informações e facilidade para expansão futura do sistema.

## Status do Projeto
 Em desenvolvimento (projeto acadêmico)
