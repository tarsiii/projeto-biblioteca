import tkinter as tk
from tkinter import messagebox


class Interface:
    def __init__(self, app):
        self.app = app

    # Tela para criar um novo usuário
    def tela_criar_usuario(self):
        self.limpar_janela()
        self.app.root.title("Criar Usuário")

        tk.Label(self.app.root, text="Nome:", font=("Arial", 14)).pack(pady=10)
        nome_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        nome_entry.pack(pady=5)

        tk.Label(self.app.root, text="Senha:", font=("Arial", 14)).pack(pady=10)
        senha_entry = tk.Entry(self.app.root, show="*", font=("Arial", 14), width=30)
        senha_entry.pack(pady=5)

        def criar_usuario():
            nome = nome_entry.get()
            senha = senha_entry.get()
            if nome and senha:
                self.app.database.adicionar_usuario(nome, senha)
                messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos")

        tk.Button(
            self.app.root,
            text="Criar",
            command=criar_usuario,
            font=("Arial", 14),
            width=10,
        ).pack(pady=20)

        # Botão para ir para a tela de login
        tk.Button(
            self.app.root,
            text="Fazer Login",
            command=self.tela_login,  # Chama a tela de login
            font=("Arial", 14),
            width=10,
        ).pack(pady=20)

    # Tela de login
    def tela_login(self):
        self.limpar_janela()
        self.app.root.title("Login")

        tk.Label(self.app.root, text="Nome:", font=("Arial", 14)).pack(pady=10)
        nome_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        nome_entry.pack(pady=5)

        tk.Label(self.app.root, text="Senha:", font=("Arial", 14)).pack(pady=10)
        senha_entry = tk.Entry(self.app.root, show="*", font=("Arial", 14), width=30)
        senha_entry.pack(pady=5)

        def fazer_login():
            nome = nome_entry.get()
            senha = senha_entry.get()
            if self.app.database.verificar_login(nome, senha):
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                self.tela_principal()
            else:
                messagebox.showerror("Erro", "Nome ou senha inválidos")

        tk.Button(
            self.app.root,
            text="Login",
            command=fazer_login,
            font=("Arial", 14),
            width=10,
        ).pack(pady=20)

    # Tela principal com funcionalidades
    def tela_principal(self):
        self.limpar_janela()
        self.app.root.title("Oxente Bibliotecas")
        self.app.root.geometry("600x500")

        tk.Label(
            self.app.root, text="Oxente Bibliotecas", font=("Arial", 24, "bold")
        ).pack(pady=20)

        # Botão para adicionar livro
        tk.Button(
            self.app.root,
            text="Adicionar Livro",
            font=("Arial", 14),
            width=25,
            command=self.tela_adicionar_livro,
        ).pack(pady=10)

        # Botão para adicionar usuário
        tk.Button(
            self.app.root,
            text="Adicionar Usuário",
            font=("Arial", 14),
            width=25,
            command=self.tela_criar_usuario,
        ).pack(pady=10)

        # Botão para cadastrar leitor
        tk.Button(
            self.app.root,
            text="Adicionar Leitor",
            font=("Arial", 14),
            width=25,
            command=self.tela_cadastrar_leitor,
        ).pack(pady=10)

        # Botão para fazer empréstimo
        tk.Button(
            self.app.root,
            text="Fazer Empréstimo de Livro",
            font=("Arial", 14),
            width=25,
            command=self.tela_emprestimo_livro,
        ).pack(pady=10)

        # Botão de sair que volta para a tela de login
        tk.Button(
            self.app.root,
            text="Sair",
            font=("Arial", 14),
            width=25,
            command=self.tela_login,
        ).pack(pady=20)

    def tela_cadastrar_leitor(self):
        self.limpar_janela()
        self.app.root.title("Cadastro de Leitor")

        # Campo Nome
        tk.Label(self.app.root, text="Nome:", font=("Arial", 14)).pack(pady=10)
        nome_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        nome_entry.pack(pady=5)

        # Campo Sobrenome
        tk.Label(self.app.root, text="Sobrenome:", font=("Arial", 14)).pack(pady=10)
        sobrenome_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        sobrenome_entry.pack(pady=5)

        # Campo Email
        tk.Label(self.app.root, text="Email:", font=("Arial", 14)).pack(pady=10)
        email_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        email_entry.pack(pady=5)

        # Função para adicionar leitor
        def cadastrar_leitor():
            nome = nome_entry.get()
            sobrenome = sobrenome_entry.get()
            email = email_entry.get()

            if nome and sobrenome and email:
                sucesso = self.app.database.adicionar_leitor(nome, sobrenome, email)
                if sucesso:
                    messagebox.showinfo("Sucesso", "Leitor cadastrado com sucesso!")
                    self.tela_principal()
                else:
                    messagebox.showerror(
                        "Erro", "Erro ao cadastrar o leitor. Tente novamente."
                    )
            else:
                messagebox.showwarning(
                    "Aviso", "Preencha todos os campos corretamente."
                )

        # Botão para cadastrar
        tk.Button(
            self.app.root,
            text="Cadastrar",
            font=("Arial", 14),
            command=cadastrar_leitor,
        ).pack(pady=20)

        # Botão para voltar
        tk.Button(
            self.app.root,
            text="Voltar",
            font=("Arial", 14),
            command=self.tela_principal,
        ).pack(pady=10)

    def tela_adicionar_livro(self):
        self.limpar_janela()
        self.app.root.title("Adicionar Livro")

        tk.Label(self.app.root, text="Título:", font=("Arial", 14)).pack(pady=10)
        titulo_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        titulo_entry.pack(pady=5)

        tk.Label(self.app.root, text="Ano de Publicação:", font=("Arial", 14)).pack(
            pady=10
        )
        ano_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        ano_entry.pack(pady=5)

        tk.Label(self.app.root, text="Nome do Autor:", font=("Arial", 14)).pack(pady=10)
        autor_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        autor_entry.pack(pady=5)

        tk.Label(self.app.root, text="Gênero:", font=("Arial", 14)).pack(pady=10)
        genero_entry = tk.Entry(self.app.root, font=("Arial", 14), width=30)
        genero_entry.pack(pady=5)

        def adicionar():
            titulo = titulo_entry.get()
            ano_publicacao = ano_entry.get()
            autor = autor_entry.get()
            genero = genero_entry.get()

            if titulo and ano_publicacao.isdigit():
                sucesso = self.app.database.adicionar_livro(
                    titulo, ano_publicacao, autor, genero
                )
                if sucesso:
                    messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
                    self.tela_principal()  # Volta para a tela principal após adicionar o livro
                else:
                    messagebox.showerror("Erro", "Erro ao adicionar o livro.")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

        tk.Button(
            self.app.root, text="Adicionar", font=("Arial", 14), command=adicionar
        ).pack(pady=20)
        tk.Button(
            self.app.root,
            text="Voltar",
            font=("Arial", 14),
            command=self.tela_principal,
        ).pack(pady=10)

    def tela_emprestimo_livro(self):
        self.limpar_janela()
        self.app.root.title("Empréstimo de Livro")

        self.app.root.geometry("800x700")

        # Função para atualizar a listbox de leitores com base na busca
        def atualizar_listbox_leitores(event=None):
            termo_busca = (
                search_leitores_entry.get().lower()
            )  # Pega o termo de busca e converte para minúsculas
            self.listbox_leitores.delete(0, tk.END)  # Limpa a listbox de leitores
            for leitor in leitores:
                nome_completo = (
                    f"{leitor['Nome']} {leitor['Sobrenome']}".lower()
                )  # Nome completo em minúsculas
                if (
                    termo_busca in nome_completo
                ):  # Verifica se o termo está contido no nome completo
                    self.listbox_leitores.insert(
                        tk.END, f"{leitor['Nome']} {leitor['Sobrenome']}"
                    )

        # Função para atualizar a listbox de livros com base na busca
        def atualizar_listbox_livros(event=None):
            termo_busca = (
                search_livros_entry.get().lower()
            )  # Pega o termo de busca e converte para minúsculas
            self.listbox_livros.delete(0, tk.END)  # Limpa a listbox de livros
            for livro in livros:
                titulo_autor = (
                    f"{livro['Titulo']} - {livro['Autor']}".lower()
                )  # Título e autor em minúsculas
                if (
                    termo_busca in titulo_autor
                ):  # Verifica se o termo está contido no título ou autor
                    self.listbox_livros.insert(
                        tk.END, f"{livro['Titulo']} - {livro['Autor']}"
                    )

        # Campo de busca para leitores
        tk.Label(self.app.root, text="Pesquisar Leitor:", font=("Arial", 14)).pack(
            pady=10
        )
        search_leitores_entry = tk.Entry(self.app.root, font=("Arial", 14), width=50)
        search_leitores_entry.pack(pady=5)
        search_leitores_entry.bind(
            "<KeyRelease>", atualizar_listbox_leitores
        )  # Atualiza a listbox a cada tecla

        # Cria um listbox para mostrar os leitores
        self.listbox_leitores = tk.Listbox(
            self.app.root, height=10, width=50, selectmode=tk.SINGLE
        )
        self.listbox_leitores.pack(pady=10)

        # Consulta os leitores cadastrados no banco de dados
        leitores = self.app.database.buscar_leitores()

        # Preenche a Listbox com os nomes dos leitores
        for leitor in leitores:
            self.listbox_leitores.insert(
                tk.END, f"{leitor['Nome']} {leitor['Sobrenome']}"
            )

        # Campo de busca para livros
        tk.Label(self.app.root, text="Pesquisar Livro:", font=("Arial", 14)).pack(
            pady=10
        )
        search_livros_entry = tk.Entry(self.app.root, font=("Arial", 14), width=50)
        search_livros_entry.pack(pady=5)
        search_livros_entry.bind(
            "<KeyRelease>", atualizar_listbox_livros
        )  # Atualiza a listbox a cada tecla

        # Cria um listbox para mostrar os livros disponíveis
        self.listbox_livros = tk.Listbox(
            self.app.root, height=10, width=50, selectmode=tk.SINGLE
        )
        self.listbox_livros.pack(pady=10)

        # Consulta os livros disponíveis no banco de dados
        livros = self.app.database.buscar_livros_disponiveis()

        # Preenche a Listbox com os títulos dos livros disponíveis
        for livro in livros:
            self.listbox_livros.insert(tk.END, f"{livro['Titulo']} - {livro['Autor']}")

        # Função para confirmar o empréstimo
        def confirmar_emprestimo():
            # Pega o índice do leitor selecionado
            leitor_index = self.listbox_leitores.curselection()
            # Pega o índice do livro selecionado
            livro_index = self.listbox_livros.curselection()

            # Verifica se algo foi selecionado em ambas as listas
            if not leitor_index or not livro_index:
                tk.messagebox.showwarning(
                    "Seleção Inválida", "Por favor, selecione um leitor e um livro."
                )
                return

            # Obtém o leitor e o livro selecionados
            leitor_selecionado = leitores[leitor_index[0]]
            livro_selecionado = livros[livro_index[0]]

            # Exibe uma mensagem de confirmação ou faz algo com os dados selecionados
            tk.messagebox.showinfo(
                "Empréstimo Confirmado",
                f"Leitor: {leitor_selecionado['Nome']} {leitor_selecionado['Sobrenome']}\n"
                f"Livro: {livro_selecionado['Titulo']} - {livro_selecionado['Autor']}",
            )

            # Aqui você pode realizar o empréstimo no banco de dados usando a lógica desejada.

        # Botão para confirmar o empréstimo
        tk.Button(
            self.app.root, text="Confirmar Empréstimo", command=confirmar_emprestimo
        ).pack(pady=10)

        # Botão para voltar para a tela principal
        tk.Button(self.app.root, text="Voltar", command=self.tela_principal).pack(
            pady=10
        )

    def confirmar_emprestimo(self):
        try:
            # Obtém o índice do leitor e livro selecionados
            indice_leitor_selecionado = self.listbox_leitores.curselection()[0]
            leitor_selecionado = self.listbox_leitores.get(indice_leitor_selecionado)

            indice_livro_selecionado = self.listbox_livros.curselection()[0]
            livro_selecionado = self.listbox_livros.get(indice_livro_selecionado)

            # Extrai o nome do leitor e título do livro
            nome_leitor = leitor_selecionado.split()[
                0
            ]  # Pega o primeiro nome do leitor
            titulo_livro = livro_selecionado.split(" - ")[0]  # Pega o título do livro

            # Faz o empréstimo do livro
            sucesso = self.app.database.fazer_emprestimo(titulo_livro, nome_leitor)

            if sucesso:
                messagebox.showinfo(
                    "Sucesso",
                    f"O livro '{titulo_livro}' foi emprestado para '{nome_leitor}' com sucesso!",
                )
                self.tela_principal()
            else:
                messagebox.showerror(
                    "Erro", "Erro ao realizar o empréstimo. Tente novamente."
                )
        except IndexError:
            messagebox.showwarning(
                "Aviso",
                "Selecione um leitor e um livro antes de confirmar o empréstimo.",
            )

    def confirmar_emprestimo(self):
        try:
            # Obtém o índice do livro selecionado
            indice_selecionado = self.listbox_livros.curselection()[0]
            livro_selecionado = self.listbox_livros.get(indice_selecionado)

            # Faz o empréstimo do livro (aqui você pode fazer uma lógica de atualização no banco)
            sucesso = self.app.database.fazer_emprestimo(livro_selecionado)

            if sucesso:
                messagebox.showinfo(
                    "Sucesso",
                    f"O livro '{livro_selecionado}' foi emprestado com sucesso!",
                )
                self.tela_principal()
            else:
                messagebox.showerror(
                    "Erro", "Erro ao realizar o empréstimo. Tente novamente."
                )
        except IndexError:
            messagebox.showwarning(
                "Aviso", "Selecione um livro antes de confirmar o empréstimo."
            )

    # Função para limpar a janela
    def limpar_janela(self):
        for widget in self.app.root.winfo_children():
            widget.destroy()
