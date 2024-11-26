import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    cidade TEXT
)
''')

# Função para criar novo cliente
def criar_cliente(nome, email, cidade):
    cursor.execute('''
    INSERT INTO clientes (nome, email, cidade)
    VALUES (?, ?, ?)
    ''', (nome, email, cidade))
    conn.commit()

# Função para ler todos os clientes
def ler_clientes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()

# Função para atualizar um cliente
def atualizar_cliente(id, nome, email, cidade):
    cursor.execute('''
    UPDATE clientes
    SET nome = ?, email = ?, cidade = ?
    WHERE id = ?
    ''', (nome, email, cidade, id))
    conn.commit()

# Função para deletar um cliente
def deletar_cliente(id):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conn.commit()

# Testar funções
criar_cliente('Carlos Silva', 'carlos.silva@example.com', 'São Paulo')
criar_cliente('Maria Oliveira', 'maria.oliveira@example.com', 'Rio de Janeiro')

clientes = ler_clientes()
print('Clientes:', clientes)

atualizar_cliente(1, 'Carlos Souza', 'carlos.souza@example.com', 'Brasília')
deletar_cliente(2)

clientes = ler_clientes()
print('Clientes Atualizados:', clientes)

# Fechar conexão
conn.close()
