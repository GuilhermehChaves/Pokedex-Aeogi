### DER banco de dados

![Diagrama pokedex](https://user-images.githubusercontent.com/48635609/70325554-0116bf00-1811-11ea-93a5-15ea85761a09.png)


### Sobre o projeto

Projeto Pokedex, realizado utilizando a linguagem python juntamente da biblioteca
Flask para desenvolvimento web, pymysql para efetuar a conexão com o banco de dados
e alguns recursos nativos presentes na própria linguagem de programação.

### Populando o banco de dados
O banco de dados utilizado para realização do projeto foi o Mysql,para configurar as informações do banco abra o arquivo /modules/db.py,
la se encontram as configurações do banco, o nome da base de dados criada é 'pokedex',
o script para execução está em pokemon.sql.

Para popular o banco de dados execute o seguinte comando no terminal, após realizada
as devidas configurações.

python fill_database.py