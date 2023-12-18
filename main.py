import tkinter as tk

root = tk.Tk()
root.title("Calculadora")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row_val = 1
col_val = 0

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

for button in buttons:
    tk.Button(root, text=button, padx=40, pady=20, command=lambda b=button: on_click(b) if b not in ['=', 'C'] else calculate() if b == '=' else clear_display()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Loop principal
root.mainloop()
    