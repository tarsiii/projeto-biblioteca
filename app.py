import tkinter as tk
import database
from login.interface import Interface


class App:
    def __init__(self, root):
        self.root = root
        self.database = database

        # Inicializa o banco de dados
        self.database.iniciar_banco()

        # Inicia a interface com base no estado do banco
        self.interface = Interface(self)

        if not self.database.existe_usuario():
            self.interface.tela_criar_usuario()
        else:
            self.interface.tela_principal()  #### ALTERAR DEPOISSSS PARA TELA LOGIN


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = App(root)
    root.mainloop()
