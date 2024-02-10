#By KotarouKatsura

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg='#F0F0F0')
        master.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry_value = ''
        tk.Entry(width=17, bg='#FFF', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            ('(', 0, 50), (')', 90, 50), ('%', 180, 50), ('1', 0, 125),
            ('2', 90, 125), ('3', 180, 125), ('4', 0, 200), ('5', 90, 200),
            ('6', 180, 200), ('7', 0, 275), ('8', 90, 275), ('9', 180, 275),
            ('0', 90, 350), ('.', 180, 350), ('+', 270, 275), ('-', 270, 200),
            ('/', 270, 50), ('x', 270, 125), ('=', 270, 350), ('C', 0, 350)
        ]

        for text, x, y in buttons:
            tk.Button(width=11, height=4, text=text, relief='flat', bg='#D3D3D3',
                      command=lambda t=text: self.handle_button_click(t)).place(x=x, y=y)

    def handle_button_click(self, value):
        if value == 'C':
            self.clear()
        elif value == '=':
            self.solve()
        else:
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.clear()


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
