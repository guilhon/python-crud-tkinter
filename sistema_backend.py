import sqlite3 as sql

class Conexao():
    base_de_dados = "d:/clientes.db"
    conn = None
    indexador = None
    connected = False

    def connect(self):
        Conexao.conn = sql.connect(Conexao.base_de_dados)
        Conexao.indexador = Conexao.conn.cursor()
        Conexao.connected = True

    def disconnect(self):
        Conexao.conn.close()
        Conexao.connected = False

    def execute(self, sql, parms = None):
        if Conexao.connected:
            if parms == None:
                Conexao.indexador.execute(sql)
            else:
                Conexao.indexador.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return Conexao.indexador.fetchall()

    def persist(self):
        if Conexao.connected:
            Conexao.conn.commit()
            return True
        else:
            return False

def initDB():
    transacao = Conexao()
    transacao.connect()
    transacao.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    transacao.persist()
    transacao.disconnect()

def insert(nome, sobrenome, email, cpf):
    transacao = Conexao()
    transacao.connect()
    transacao.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
    transacao.persist()
    transacao.disconnect()

def view():
    transacao = Conexao()
    transacao.connect()
    transacao.execute("SELECT * FROM clientes")
    rows = transacao.fetchall()
    transacao.disconnect()
    return rows

def search(nome="", sobrenome="", email="", cpf=""
    ):
    transacao = Conexao()
    transacao.connect()
    transacao.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome,sobrenome,email, cpf))
    rows = transacao.fetchall()
    transacao.disconnect()
    return rows

def delete(id):
    transacao = Conexao()
    transacao.connect()
    transacao.execute("DELETE FROM clientes WHERE id = ?", (id,))
    transacao.persist()
    transacao.disconnect()

def update(id, nome, sobrenome, email, cpf):
    transacao = Conexao()
    transacao.connect()
    transacao.execute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=? WHERE id = ?",(nome, sobrenome,email, cpf, id))
    transacao.persist()
    transacao.disconnect()

initDB()


