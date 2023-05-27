import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


class AplicativoPlanejadorEstudos:
    def __init__(self, root):
        self.root = root
        self.root.title("Planejador de Estudos")

        # Lista para armazenar as tarefas
        self.tarefas = []

        # Componentes da interface
        tk.Label(root, text="Tarefa:").grid(row=0, column=0, sticky=tk.W)
        self.entrada_tarefa = tk.Entry(root, width=30)
        self.entrada_tarefa.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Hora de Início:").grid(row=1, column=0, sticky=tk.W)
        self.entrada_hora_inicio = tk.Entry(root, width=10)
        self.entrada_hora_inicio.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Hora de Término:").grid(row=2, column=0, sticky=tk.W)
        self.entrada_hora_termino = tk.Entry(root, width=10)
        self.entrada_hora_termino.grid(row=2, column=1, padx=10, pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.botao_programacao = tk.Button(root, text="Gerar Programação", command=self.gerar_programacao)
        self.botao_programacao.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        hora_inicio = self.entrada_hora_inicio.get()
        hora_termino = self.entrada_hora_termino.get()

        if tarefa and hora_inicio and hora_termino:
            for tarefa_existente in self.tarefas:
                _, hora_inicio_existente, hora_termino_existente = tarefa_existente
                if hora_termino == hora_termino_existente:
                    messagebox.showerror("Erro", "Conflito de horários. Por favor, escolha um horário diferente.")
                    return

            self.tarefas.append((tarefa, hora_inicio, hora_termino))
            messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
            self.entrada_tarefa.delete(0, tk.END)
            self.entrada_hora_inicio.delete(0, tk.END)
            self.entrada_hora_termino.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def gerar_programacao(self):
        if len(self.tarefas) == 0:
            messagebox.showerror("Erro", "Por favor, adicione pelo menos uma tarefa.")
        else:
            self.tarefas.sort(key=lambda x: x[2])  # Ordena as tarefas com base no horário de término

            programacao = self.agendamento_intervalo(self.tarefas)
            if programacao:
                messagebox.showinfo("Programação Gerada", programacao)
            else:
                messagebox.showerror("Erro", "Não foi possível gerar uma programação válida.")

    def agendamento_intervalo(self, tarefas):
        programacao = []

        for tarefa in tarefas:
            nome_tarefa, hora_inicio, hora_termino = tarefa

            # Converte as strings de tempo em objetos datetime
            hora_inicio = datetime.strptime(hora_inicio, "%H:%M")
            hora_termino = datetime.strptime(hora_termino, "%H:%M")

            if hora_termino <= hora_inicio:
                messagebox.showerror("Erro", f"A tarefa '{nome_tarefa}' tem uma hora de término anterior à hora de início.")
                return None

            programacao.append(f"{hora_inicio.strftime('%H:%M')} - {hora_termino.strftime('%H:%M')}: {nome_tarefa}")

        return "\n".join(programacao)


root = tk.Tk()
app = AplicativoPlanejadorEstudos(root)
root.mainloop()
