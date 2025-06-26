import sqlite3  # Biblioteca para acessar banco de dados SQLite
import pandas as pd  # Biblioteca para manipular dados em formato de tabela

# Nome do arquivo do banco de dados
DB_NAME = 'credenciamento.db'

# Cria a tabela 'alunos' se ainda não existir
def criar_tabela():
    connection_bd = sqlite3.connect(DB_NAME)  # Conecta ao banco
    connection_cursor = connection_bd.cursor()  # Cria um cursor para executar comandos SQL
    
    # Cria a tabela com colunas: id, nome, idade, grau, genero
    connection_cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        grau TEXT,
        genero TEXT
    )
    ''')
    connection_bd.commit()  # Salva as alterações
    connection_bd.close()  # Fecha a conexão com o banco

# Adiciona um novo aluno ao banco de dados
def adicionar_aluno(nome, idade, grau, genero):
    connection_bd = sqlite3.connect(DB_NAME)
    connection_cursor = connection_bd.cursor()

    # Insere os dados do aluno na tabela
    connection_cursor.execute(
        "INSERT INTO alunos (nome, idade, grau, genero) VALUES (?, ?, ?, ?)",
        (nome, idade, grau, genero)
    )
    connection_bd.commit()
    connection_bd.close()

# Retorna todos os dados da tabela como um DataFrame (usado para exibir no Streamlit)
def visualizar_dados():
    connection_bd = sqlite3.connect(DB_NAME)
    
    # Executa a consulta SQL e armazena os dados em um DataFrame
    df = pd.read_sql_query("SELECT * FROM alunos", connection_bd)

    connection_bd.close()
    return df  # Retorna o DataFrame com os dados

# Busca um aluno pelo nome (sem diferenciar maiúsculas/minúsculas)
def buscar_aluno(nome):
    connection_bd = sqlite3.connect(DB_NAME)
    connection_cursor = connection_bd.cursor()

    # Busca por nome ignorando maiúsculas/minúsculas
    connection_cursor.execute(
        "SELECT * FROM alunos WHERE LOWER(nome) = LOWER(?)",
        (nome,)
    )
    resultado = connection_cursor.fetchone()  # Retorna só o primeiro resultado encontrado
    connection_bd.close()
    return resultado  # Retorna como tupla (id, nome, idade, grau, genero)

# Atualiza os dados de um aluno com base no ID
def atualizar_aluno(id_aluno, novo_nome, nova_idade, novo_grau, novo_genero):
    conection_bd = sqlite3.connect(DB_NAME)
    conection_cursor = conection_bd.cursor()

    # Atualiza os campos com os novos valores
    conection_cursor.execute('''
        UPDATE alunos
        SET nome = ?, idade = ?, grau = ?, genero = ?
        WHERE id = ?
    ''', (novo_nome, nova_idade, novo_grau, novo_genero, id_aluno))

    conection_bd.commit()
    conection_bd.close()

# Remove um aluno com base no ID
def excluir_aluno(id_aluno):
    connection_bd = sqlite3.connect(DB_NAME)
    connection_cursor = connection_bd.cursor()

    # Deleta o aluno pelo ID
    connection_cursor.execute(
        "DELETE FROM alunos WHERE id = ?",
        (id_aluno,)  # Importante: usar vírgula para formar tupla
    )

    connection_bd.commit()
    connection_bd.close()
