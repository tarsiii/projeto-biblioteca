import pg8000


def conectar():
    conexao = pg8000.connect(
        host="localhost", database="postgres", user="postgres", password="pabd"
    )
    return conexao


def iniciar_banco():
    con = conectar()
    cursor = con.cursor()

    # Criação da tabela Livros
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Livros (
            LivroID SERIAL PRIMARY KEY NOT NULL,
            Titulo VARCHAR(255) NOT NULL,
            AnoPublicacao INT,
            Autor VARCHAR(255),
            Genero VARCHAR(255),
            Disponivel INT DEFAULT 1
        );
        """
    )

    # Criação da tabela Leitores
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Leitores (
            LeitorID SERIAL PRIMARY KEY NOT NULL,
            Nome VARCHAR(100) NOT NULL,
            Sobrenome VARCHAR(100) NOT NULL,
            Email VARCHAR(255) NOT NULL UNIQUE
        );
        """
    )

    # Criação da tabela Usuarios
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Usuarios (
            id SERIAL PRIMARY KEY NOT NULL,
            Nome VARCHAR(100) NOT NULL,
            Senha VARCHAR(100) NOT NULL
        );
        """
    )

    # Criação da tabela Emprestimos
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Emprestimos (
            EmprestimoID SERIAL PRIMARY KEY,
            LivroID INT NOT NULL,
            LeitorID INT NOT NULL,
            DataEmprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            DataDevolucao TIMESTAMP NULL,
            FOREIGN KEY (LivroID) REFERENCES Livros (LivroID),
            FOREIGN KEY (LeitorID) REFERENCES Leitores (LeitorID)
        );
        """
    )
    con.commit()
    cursor.close()
    con.close()
    return True


def existe_usuario():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM Usuarios")
    conta = cursor.fetchone()[0]
    cursor.close()
    con.close()
    return conta


def adicionar_usuario(nome, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO Usuarios (Nome, Senha) VALUES (%s, %s)", (nome, senha))
    con.commit()
    cursor.close()
    con.close()


def adicionar_leitor(nome, sobrenome, email):
    con = conectar()
    cursor = con.cursor()
    try:
        cursor.execute(
            "INSERT INTO Leitores (Nome, Sobrenome, Email) VALUES (%s, %s, %s)",
            (nome, sobrenome, email),
        )
        con.commit()
        return True
    except Exception as e:
        print(f"Erro ao adicionar leitor: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()


def verificar_login(nome, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM Usuarios WHERE Nome = %s AND Senha = %s", (nome, senha)
    )
    resultado = cursor.fetchone()[0]
    cursor.close()
    con.close()

    # Se o resultado for 1, o login está correto, retorna True
    if resultado == 1:
        return True
    else:
        return False


def buscar_leitores():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT Nome, Sobrenome FROM Leitores")
    leitores = cursor.fetchall()
    cursor.close()
    con.close()
    return [{"Nome": leitor[0], "Sobrenome": leitor[1]} for leitor in leitores]


def fazer_emprestimo(titulo, nome_leitor):
    con = conectar()
    cursor = con.cursor()

    try:
        # Atualiza a tabela Livros para marcar o livro como indisponível
        cursor.execute("UPDATE Livros SET Disponivel = 0 WHERE Titulo = %s", (titulo,))
        
        # Adiciona o empréstimo na tabela Emprestimos
        cursor.execute("""
            INSERT INTO Emprestimos (LivroID, LeitorID)
            SELECT l.LivroID, le.LeitorID
            FROM Livros l, Leitores le
            WHERE l.Titulo = %s AND le.Nome = %s
        """, (titulo, nome_leitor))

        con.commit()
        return True
    except Exception as e:
        print(f"Erro ao fazer o empréstimo: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()



def adicionar_livro(titulo, ano_publicacao, autor_id, genero_id):
    con = conectar()
    cursor = con.cursor()
    try:
        cursor.execute(
            "INSERT INTO Livros (Titulo, AnoPublicacao, Autor, Genero) VALUES (%s, %s, %s, %s)",
            (titulo, ano_publicacao, autor_id, genero_id),
        )
        con.commit()
        return True
    except Exception as e:
        print(f"Erro ao adicionar livro: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()


def buscar_livros_disponiveis():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT Titulo, Autor FROM Livros WHERE Disponivel = 1")
    livros = cursor.fetchall()
    cursor.close()
    con.close()
    return [{"Titulo": livro[0], "Autor": livro[1]} for livro in livros]


def fazer_emprestimo(titulo):
    con = conectar()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE Livros SET Disponivel = 0 WHERE Titulo = %s", (titulo,))
        con.commit()
        return True
    except Exception as e:
        print(f"Erro ao fazer o empréstimo: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()
