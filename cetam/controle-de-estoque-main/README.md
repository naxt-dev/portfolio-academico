# 📦 Sistema de Controle de Estoque

Este projeto foi desenvolvido como parte das atividades do componente curricular de **Linguagem de Programação em PHP**. Trata-se de um sistema web completo para o gerenciamento e controle de estoque, fornecedores, lojas, produtos e usuários.

## 🛠️ Requisitos do Ambiente
Para rodar este projeto, você precisa de um ambiente de desenvolvimento local que suporte PHP e MySQL.
* **Recomendação:** XAMPP ou WampServer.

## 🚀 Como Configurar e Executar

1. **Baixe o repositório** com os arquivos do projeto.
2. **Mova para o servidor local:** Descompacte os arquivos no diretório público do seu servidor web:
   * No Windows (XAMPP): `C:\xampp\htdocs\`
   * No Linux: `/opt/lampp/htdocs/` ou `/var/www/html/`
3. **Renomeie a pasta** descompactada para `controle-de-estoque`.
4. **Ligue o servidor:** Abra o painel de controle do seu servidor local (ex: XAMPP) e inicie os módulos **Apache** e **MySQL**.
5. **Banco de Dados:** Importe o arquivo SQL (localizado na pasta `/dumps`) para o seu gerenciador de banco de dados (como o phpMyAdmin) para criar as tabelas necessárias.
6. **Acesse a aplicação:** Abra o seu navegador e digite a seguinte URL:
   `http://localhost/controle-de-estoque`

## 📂 Estrutura de Diretórios
Abaixo está a organização principal dos arquivos do sistema:

* `/config`: Arquivos de configuração e conexão com o banco de dados.
* `/dumps`: Scripts SQL para importação e restauração do banco de dados.
* `/estoque`, `/fornecedores`, `/lojas`, `/produtos`, `/usuarios`: Pastas contendo a lógica e as interfaces de cada módulo do CRUD.
* `/includes`: Trechos de código reutilizáveis (como headers e footers).
* `/css`, `/js`, `/images`: Arquivos estáticos de front-end.
* `index.php`: Página inicial do sistema.
* `login.php` / `logout.php`: Sistema de autenticação de usuários.
