import database


def deletar_banco():
    con = database.conectar()
    cursor = con.cursor()
    try:
        cursor.execute(
            """
            DROP TABLE IF EXISTS Livros CASCADE;
            DROP TABLE IF EXISTS Leitores CASCADE;
            DROP TABLE IF EXISTS Usuarios CASCADE;
            """
        )
        con.commit()
        return True
    except Exception as e:
        print(f"Erro ao deletar banco: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()


def adicionar_varios_livros(livros):
    con = database.conectar()
    cursor = con.cursor()

    try:
        # Adiciona os livros, autores e gêneros
        query_livro = """
            INSERT INTO Livros (Titulo, AnoPublicacao, Autor, Genero)
            VALUES (%s, %s, %s, %s)
        """

        livros_dados = [
            (livro["titulo"], livro["ano_publicacao"], livro["autor"], livro["genero"])
            for livro in livros
        ]

        cursor.executemany(query_livro, livros_dados)

        con.commit()
        print("Livros adicionados com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao adicionar livros: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()

# adicione esses livros
livros = [
    {
        "titulo": "O Senhor dos Anéis",
        "ano_publicacao": "1954",
        "autor": "J.R.R. Tolkien",
        "genero": "Fantasia",
    },
    {
        "titulo": "1984",
        "ano_publicacao": "1949",
        "autor": "George Orwell",
        "genero": "Distopia",
    },
    {
        "titulo": "Dom Casmurro",
        "ano_publicacao": "1899",
        "autor": "Machado de Assis",
        "genero": "Romance",
    },
    {
        "titulo": "O Pequeno Príncipe",
        "ano_publicacao": "1943",
        "autor": "Antoine de Saint-Exupéry",
        "genero": "Ficção",
    },
    {
        "titulo": "Cem Anos de Solidão",
        "ano_publicacao": "1967",
        "autor": "Gabriel García Márquez",
        "genero": "Realismo Mágico",
    },
    {
        "titulo": "Crime e Castigo",
        "ano_publicacao": "1866",
        "autor": "Fiódor Dostoiévski",
        "genero": "Romance psicológico",
    },
    {
        "titulo": "A Revolução dos Bichos",
        "ano_publicacao": "1945",
        "autor": "George Orwell",
        "genero": "Distopia",
    },
    {
        "titulo": "O Apanhador no Campo de Centeio",
        "ano_publicacao": "1951",
        "autor": "J.D. Salinger",
        "genero": "Ficção",
    },
    {
        "titulo": "Moby Dick",
        "ano_publicacao": "1851",
        "autor": "Herman Melville",
        "genero": "Aventura",
    },
    {
        "titulo": "Orgulho e Preconceito",
        "ano_publicacao": "1813",
        "autor": "Jane Austen",
        "genero": "Romance",
    },
    {
        "titulo": "Ulisses",
        "ano_publicacao": "1922",
        "autor": "James Joyce",
        "genero": "Ficção Moderna",
    },
    {
        "titulo": "As Crônicas de Nárnia",
        "ano_publicacao": "1950",
        "autor": "C.S. Lewis",
        "genero": "Fantasia",
    }
]


# deletar_banco()

# adicionar_varios_livros(livros)