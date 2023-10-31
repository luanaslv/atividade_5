# Nesta etapa importamos a biblioteca Tkinter, renomeando-a para tk, importando os demais arquivos
import tkinter as tk
from candidato import CandidatoApp
from recrutador import RecrutadorApp

#criação da classe IndexApp que representa a janela princial e suas funções
class IndexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela Inicial")

        candidato_button = tk.Button(self.master, text="Sou candidato", command=self.open_candidato)
        candidato_button.pack()

        recrutador_button = tk.Button(self.master, text="Sou recrutador", command=self.open_recrutador)
        recrutador_button.pack()

    def open_candidato(self):
        candidato_app = tk.Tk()
        CandidatoApp(candidato_app)

    def open_recrutador(self):
        recrutador_app = tk.Tk()
        RecrutadorApp(recrutador_app)

#iniciação do loop principal 
def main():
    app = tk.Tk()
    IndexApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()