# CRM para Corretor de Planos de Saúde

## Proposta do Sistema

Este projeto tem como objetivo desenvolver um sistema CRM (Customer Relationship Management) voltado para um corretor autônomo de planos de saúde. A aplicação permite o gerenciamento eficiente de clientes, possibilitando o cadastro, visualização e organização de informações, facilitando o acompanhamento e atendimento dos mesmos.

## Objetivo

Construir um sistema web funcional que integre frontend, backend e banco de dados, aplicando conceitos de engenharia de software e diferentes paradigmas de programação.

## Equipe de Desenvolvimento

Backend:

Emilly Karoline Cunha Fernandes
  Responsável pela implementação do servidor utilizando Flask, integração com o banco de dados MySQL e lógica de negócio do sistema.

Frontend:

Thierry Hanry Ribeiro da Silva Cardoso
  Responsável pela criação da interface do usuário utilizando HTML e CSS, garantindo uma boa experiência visual e usabilidade.

## Tecnologias Utilizadas
- Python
- Flask
- MySQL
- HTML
- CSS

## Ferramentas
- Git
- GitHub
- Visual Studio Code

## Funcionalidades Implementadas

* Cadastro de clientes via formulário web
* Armazenamento persistente em banco de dados MySQL
* Listagem dinâmica de clientes na interface
* Integração completa entre frontend e backend
* Atualização automática da tabela após inserção de dados

## Funcionalidades em Desenvolvimento

* Sistema de autenticação (login real)
* Edição de clientes (Update)
* Exclusão de clientes (Delete)
* Dashboard com métricas e indicadores
* Sistema de alertas e acompanhamento de retornos

## Arquitetura e Paradigmas Utilizados

O projeto integra diferentes paradigmas de programação:

### Programação Procedural

Utilizada na definição das rotas e funções do backend (Flask).

### Programação Orientada a Dados

Aplicada na modelagem e manipulação do banco de dados MySQL.



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


### 4. Configurar o banco de dados

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

### 5. Executar a aplicação

bash
python app.py


Acesse no navegador:


http://127.0.0.1:5000


## Roadmap do Projeto

### Etapa Atual

* Estrutura base funcional
* Integração entre frontend e backend
* Persistência de dados

## Modelagem do Banco de Dados (Planejada)

Além da tabela de clientes já implementada, o sistema está sendo planejado para incluir outras entidades, como:

- Negociações
- Cobranças
- Alertas de retorno
- Usuários (login do corretor)

## 🗺️ Roadmap do Projeto

### Etapa Atual

* Estrutura base funcional
* Integração entre frontend e backend
* Persistência de dados

### Próximas Etapas

* Implementação de autenticação completa
* CRUD completo (Create, Read, Update, Delete)
* Dashboard interativo
* Melhorias de usabilidade e experiência do usuário

## Status do Projeto
 Em desenvolvimento (projeto acadêmico)

A versão atual contempla funcionalidades essenciais de cadastro e listagem de clientes, com evolução planejada para um sistema completo de CRM.