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

        tk.Label(root, text="Data:").grid(row=1, column=0, sticky=tk.W)
        self.entrada_data = tk.Entry(root, width=10)
        self.entrada_data.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Hora de Início:").grid(row=2, column=0, sticky=tk.W)
        self.entrada_hora_inicio = tk.Entry(root, width=10)
        self.entrada_hora_inicio.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Hora de Término:").grid(row=3, column=0, sticky=tk.W)
        self.entrada_hora_termino = tk.Entry(root, width=10)
        self.entrada_hora_termino.grid(row=3, column=1, padx=10, pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.botao_programacao = tk.Button(root, text="Gerar Programação", command=self.gerar_programacao)
        self.botao_programacao.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        data = self.entrada_data.get()
        hora_inicio = self.entrada_hora_inicio.get()
        hora_termino = self.entrada_hora_termino.get()

        if tarefa and data and hora_inicio and hora_termino:
            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
                hora_inicio = datetime.strptime(hora_inicio, "%H:%M").time()
                hora_termino = datetime.strptime(hora_termino, "%H:%M").time()
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira os dados corretamente.")
                return

            if hora_termino <= hora_inicio:
                messagebox.showerror("Erro", "A hora de término deve ser posterior à hora de início.")
                return

            for tarefa_existente in self.tarefas:
                _, data_existente, hora_inicio_existente, hora_termino_existente = tarefa_existente
                if data_existente != data:
                    continue
                if hora_termino_existente <= hora_inicio or hora_inicio_existente >= hora_termino:
                    continue
                else:
                    messagebox.showerror("Erro", "Conflito de horários. Por favor, escolha um horário diferente.")
                    return

            self.tarefas.append((tarefa, data, hora_inicio, hora_termino))
            messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def gerar_programacao(self):
        if len(self.tarefas) == 0:
            messagebox.showerror("Erro", "Por favor, adicione pelo menos uma tarefa.")
        else:
            self.tarefas.sort(key=lambda x: (x[1], x[3]))  # Ordena as tarefas com base na data e no horário de término

            programacao = self.agendamento_intervalo(self.tarefas)
            if programacao:
                messagebox.showinfo("Programação Gerada", programacao)
            else:
                messagebox.showerror("Erro", "Não foi possível gerar uma programação válida.")

    def agendamento_intervalo(self, tarefas):
        programacao = []

        for tarefa in tarefas:
            nome_tarefa, data, hora_inicio, hora_termino = tarefa
            programacao.append(f"{data.strftime('%d/%m/%Y')} - {hora_inicio.strftime('%H:%M')} - {hora_termino.strftime('%H:%M')}: {nome_tarefa}")

        return "\n".join(programacao)

    def limpar_campos(self):
        self.entrada_tarefa.delete(0, tk.END)
        self.entrada_data.delete(0, tk.END)
        self.entrada_hora_inicio.delete(0, tk.END)
        self.entrada_hora_termino.delete(0, tk.END)


root = tk.Tk()
app = AplicativoPlanejadorEstudos(root)
root.mainloop()
