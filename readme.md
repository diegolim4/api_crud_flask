# CRUD em Flask

- Projetinho para fins de estudo, conhecer o Flask e futuras consultas

## Configuração do Ambiente

- Certifique-se de ter o Python e o Pip instalado

- Crie um arquivo .env na raiz do seu projeto e configure a variável DATABASE_URL
Ex:
- DATABASE_URL="postgres://postgres:YOUR_PSW@localhost:5432/YOUR_TABLE"

## Instalação das Dependências:

- pip install -r requirements.txt

## Executando o Aplicativo:
- flask run

## Endpoints/API
- estará disponível em _http://127.0.0.1:5000_

- *GET* /api/about: testar
- *POST* /api/insert_user: Inserir usuário no banco de dados passando no body o name.
- *GET* /api/all_users: Traz todos os usuários que estão salvos no banco de dados.
- *PUT* /api/update_user: Atualiza o usuário passando por parâmetro, na URL o id e no body o name.
- *DELETE* /api/delete_user: Deleta o usuário passando por parâmetro, na URL o ID.







