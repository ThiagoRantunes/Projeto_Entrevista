import mysql.connector

class MysqlComands():

    # Função que exclui o database e o cadastra novamente ao inicializar o codigo

    def resetarBanco(self):
        self.reset_conexao = mysql.connector.connect(host = "localhost", user = "root", password = "")
        self.reset_cursor = self.reset_conexao.cursor()
        self.reset_cursor.execute("DROP DATABASE IF EXISTS curriculos_bd")
        self.reset_cursor.execute("CREATE DATABASE curriculos_bd")

    # Coexao com o banco de dados

    def connect(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    # Criando a tabela no database e inserindo os valores

    def __init__(self, host, user, password, database):
        self.resetarBanco()
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = self.connect()
        self.resetarBanco()

        self.cursor = self.conexao.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            telefone INT,
            minibio VARCHAR(255),
            entrevista INT CHECK (entrevista >= 1 AND entrevista <= 10),
            teste_teorico INT CHECK (teste_teorico >= 1 AND teste_teorico <= 10),
            teste_pratico INT CHECK (teste_pratico >= 1 AND teste_pratico <= 10),
            soft_skills INT CHECK (soft_skills >= 1 AND soft_skills <= 10)
            )""")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Thiago', 15999999999, 'Sou programador', 10, 9, 8, 10)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Gloria', 15999999999, 'Sou programador', 1, 9, 6, 2)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Nivaldo', 15999999999, 'Sou programador', 10, 4, 2, 7)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('VItor', 15999999999,'Sou programador', 10, 9, 8, 9)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Luiz', 15999999999, 'Sou programador', 8, 5, 2, 3)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Muril', 15999999999, 'Sou programador', 1, 3, 5, 2)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Dolly', 15999999999, 'Sou programador', 10, 9, 10, 10)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('João', 15999999999, 'Sou programador', 7, 9, 3, 10)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Otavio', 15999999999, 'Sou programador', 10, 2, 3, 6)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Ana', 15999999999, 'Sou programador', 3, 9, 8, 3)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Friser', 15999999999, 'Sou programador', 6, 3, 7, 1)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Carlos', 15999999999, 'Sou programador', 3, 5, 8, 4)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Giovana', 15999999999, 'Sou programador', 2, 5, 8, 10)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Patric', 15999999999, 'Sou programador', 4, 9, 8, 6)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Fernando', 15999999999, 'Sou programador', 10, 9, 4, 3)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Ashley', 15999999999, 'Sou programador', 6, 5, 4, 10)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Camile', 15999999999, 'Sou programador', 8, 6, 8, 3)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Pedro', 15999999999, 'Sou programador', 4, 9, 8, 3)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Gordola', 15999999999, 'Sou programador', 8, 9, 8, 5)")
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Magrão', 15999999999, 'Sou programador', 4, 6, 8, 7)")
        self.conexao.commit()

    # Função de cadastrar

    def insert(self, nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skill):
        self.cursor.execute(f"INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('{nome}', {telefone}, '{minibio}', {entrevista}, {teste_teorico}, {teste_pratico}, {soft_skill})")
        self.conexao.commit()

    # Função de selecionar 

    def get(self):
        self.cursor.execute("SELECT * FROM usuarios")
        self.dados = self.cursor.fetchall()
        self.lista = []
        for i in self.dados:
            self.lista.append(i)
        self.conexao.commit()
        return self.lista

    # Função de selecionar filtrando as notas

    def get_filtrado(self, entrevista, teste_teorico, teste_pratico, soft_skill):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE entrevista >= {entrevista} AND teste_teorico >= {teste_teorico} AND teste_pratico >= {teste_pratico} AND soft_skills >= {soft_skill}")
        self.dados_filtrado = self.cursor.fetchall()
        self.lista_filtrado = []
        for i in self.dados_filtrado:
            self.lista_filtrado.append(i)
        self.conexao.commit()
        return self.lista_filtrado