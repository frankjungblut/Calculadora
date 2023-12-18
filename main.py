import tkinter as tk

def on_click(char):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + char)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def clear_display():
    display.delete(0, tk.END)

def on_key_press(event):
    char = event.char
    if char.isdigit() or char in ['+', '-', '*', '/']:
        current_text = display.get()
        # Verifica se o último caractere já é o que está sendo inserido para evitar duplicação
        if not current_text.endswith(char):
            on_click(char)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym in ['BackSpace', 'Delete']:
        clear_display()

janela = tk.Tk()
janela.title("Calculadora")
janela.bind('<Key>', on_key_press)

display = tk.Entry(janela, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
display.focus_set()  # Foco no display para capturar os eventos do teclado

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row_val = 1
col_val = 0

for button in buttons:
    b = tk.Button(janela, text=button, padx=40, pady=20, command=lambda b=button: on_click(b) if b not in ['=', 'C'] else calculate() if b == '=' else clear_display())
    b.grid(row=row_val, column=col_val, sticky='nsew')
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
        janela.grid_rowconfigure(row_val, weight=1)

janela.mainloop()
