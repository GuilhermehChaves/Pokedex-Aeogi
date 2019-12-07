## DER banco de dados

![Diagrama pokedex](https://user-images.githubusercontent.com/48635609/70325554-0116bf00-1811-11ea-93a5-15ea85761a09.png)


## Sobre o projeto

Projeto Pokedex, realizado utilizando a linguagem python juntamente da biblioteca
Flask para desenvolvimento web, pymysql para efetuar a conexão com o banco de dados
e alguns recursos nativos presentes na própria linguagem de programação.

## Instalando dependencias
Para instalar as devidas dependencias execute no terminal o comando a seguir:

**pip3 install -r requirements.txt**



## Populando o banco de dados
O banco de dados utilizado para realização do projeto foi o Mysql,para configurar as informações do banco abra o arquivo **/modules/db.py**,
la se encontram as configurações do banco, o nome da base de dados criada é 'pokedex',
o script para execução está em pokemon.sql.

Para popular o banco de dados execute o seguinte comando no terminal, após realizada
as devidas configurações:

**python3 fill_database.py**


## Iniciando o projeto
Para a inicialização do projeto execute no terminal o seguint comando:


**python3 __init__.py**

**OBS: O arquivo init tem 2 underlines antes e depois, que não deram para mostrar por formatação do README**

O projeto começará a execução em http://localhost:5000
