import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.bind('<Key>', self.on_key_press)

        self.create_display()
        self.create_buttons()

    def create_display(self):
        style = ttk.Style()
        style.configure('TEntry', borderwidth=0, highlightthickness=0)
        self.display = ttk.Entry(self.master, width=35, style='TEntry', font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
        self.display.focus_set()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/',
            '.', '(', ')', '^'  # Adicionando novos botões
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            cmd = lambda x=button: self.on_click(x)
            b = tk.Button(self.master, text=button, padx=20, pady=20, command=cmd)
            b.grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
            self.master.grid_rowconfigure(row_val, weight=1)
            self.master.grid_columnconfigure(col_val, weight=1)

    def on_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear_display()
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current_text + char)

    def calculate(self):
        try:
            result = eval(self.display.get().replace('^', '**'))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro")

    def clear_display(self):
        self.display.delete(0, tk.END)

    def on_key_press(self, event):
        char = event.char
        if char.isdigit() or char in ['+', '-', '*', '/', '.', '(', ')']:
            self.on_click(char)
        elif event.keysym == 'Return':
            self.calculate()
        elif event.keysym in ['BackSpace', 'Delete']:
            self.clear_display()
        elif char == '^':
            self.on_click('^')

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
