import tkinter as tk
from tkinter import messagebox

class CronometroPomodoro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro Pomodoro")
        self.master.config(bg="#f7f5dd")  # Cor de fundo da janela

        # Configurações de tempo
        self.work_time = 25 * 60  # 25 minutos
        self.break_time = 5 * 60  # 5 minutos
        self.long_break_time = 15 * 60  # 15 minutos
        self.reps = 0
        self.running = False
        self.timer_id = None

        # Interface gráfica
        self.label = tk.Label(master, text="CRONÔMETRO POMODORO", font=("Helvetica", 24, "bold"), bg="#f7f5dd", fg="#333")
        self.label.pack(pady=10)

        self.time_label = tk.Label(master, text="25:00", font=("Helvetica", 48, "bold"), bg="#f7f5dd", fg="#333", relief="groove", bd=5)
        self.time_label.pack(pady=20)

        # Botão "Começar" com animação
        self.start_button = tk.Button(master, text="Começar", font=("Helvetica", 14), bg="#4caf50", fg="white", activebackground="#45a049", activeforeground="white", command=self.comecar_cronometro)
        self.start_button.pack(pady=10)
        self.start_button.bind("<Enter>", lambda e: self.start_button.config(bg="#45a049"))
        self.start_button.bind("<Leave>", lambda e: self.start_button.config(bg="#4caf50"))

        # Botão "Reiniciar" com animação
        self.reset_button = tk.Button(master, text="Reiniciar", font=("Helvetica", 14), bg="#f44336", fg="white", activebackground="#e53935", activeforeground="white", command=self.reiniciar_tempo)
        self.reset_button.pack(pady=10)
        self.reset_button.bind("<Enter>", lambda e: self.reset_button.config(bg="#e53935"))
        self.reset_button.bind("<Leave>", lambda e: self.reset_button.config(bg="#f44336"))

    def comecar_cronometro(self):
        if self.running:
            self.reiniciar_tempo()

        self.running = True
        self.reps += 1

        # Alterna entre trabalho, pausas curtas e pausas longas
        if self.reps % 8 == 0:  # Após 4 ciclos de trabalho, pausa longa
            self.cronometro(self.long_break_time, "Pausa Longa", "#ff9800")
        elif self.reps % 2 == 0:  # Após cada ciclo de trabalho, pausa curta
            self.cronometro(self.break_time, "Pausa Curta", "#03a9f4")
        else:  # Ciclo de trabalho
            self.cronometro(self.work_time, "Trabalhar!", "#4caf50")

    def cronometro(self, count, label_text, color):
        self.label.config(text=label_text, fg=color)
        self.time_label.config(fg=color)
        mins, secs = divmod(count, 60)
        time_str = f"{mins:02}:{secs:02}"
        self.time_label.config(text=time_str)

        if count > 0:
            self.timer_id = self.master.after(1000, self.cronometro, count - 1, label_text, color)
        else:
            self.running = False
            if label_text == "Trabalhar!":
                messagebox.showinfo("Pomodoro completado", "Hora de descansar!")
                self.comecar_cronometro()  # Inicia a pausa curta automaticamente
            elif label_text == "Pausa Curta":
                messagebox.showinfo("Descanso acabou!", "Volte ao trabalho!")
                self.comecar_cronometro()  # Inicia o próximo ciclo de trabalho
            elif label_text == "Pausa Longa":
                messagebox.showinfo("Pausa longa acabou", "Volte ao trabalho!")
                self.comecar_cronometro()  # Reinicia o ciclo de trabalho

    def reiniciar_tempo(self):
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None

        self.reps = 0
        self.running = False
        self.label.config(text="CRONÔMETRO POMODORO", fg="#333")
        self.time_label.config(text="25:00", fg="#333")

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro = CronometroPomodoro(root)
    root.mainloop()
