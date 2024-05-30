import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x600")
        root.resizable(False, False)
        
        self.style = tb.Style(theme='vapor')
        
        self.expression = ""
        self.text_input = tk.StringVar()
        
        self.entry = ttk.Entry(root, textvariable=self.text_input, font=('Arial', 24), justify='right', state='readonly')
        self.entry.grid(row=0, column=0, columnspan=5, pady=20, padx=10, ipady=10, sticky="nsew")
        
        self.create_buttons()
        
    def create_buttons(self):
        
        self.style.configure('Large.TButton', font=('Arial', 18), padding=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('ln', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('(', 5, 3), (')', 5, 4),
            ('C', 6, 0, 3), ('D', 6, 3, 2)
        ]
        
        for button in buttons:
            if len(button) == 3:
                text, row, col = button
                self.add_button(text, row, col)
            elif len(button) == 4:
                text, row, col, cs = button
                self.add_button(text, row, col, cs)
        
    
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.root.grid_columnconfigure(j, weight=1)
            
    def add_button(self, text, row, col, cs=1):
        button = ttk.Button(
            self.root, text=text, command=lambda t=text: self.on_button_click(t), 
            bootstyle="info-outline", style='Large.TButton'
        )
        button.grid(row=row, column=col, columnspan=cs, sticky="nsew", padx=5, pady=5)
        
    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "D":
            self.delete_last()
        elif char == "C":
            self.clear_all()
        elif char == "log":
            self.expression += "math.log10("
            self.text_input.set(self.expression)
        elif char == "ln":
            self.expression += "math.log("
            self.text_input.set(self.expression)
        elif char in ["sin", "cos", "tan"]:
            self.expression += f"math.{char}(math.radians("
            self.text_input.set(self.expression)
        elif char == "sqrt":
            self.expression += "math.sqrt("
            self.text_input.set(self.expression)
        elif char == "^":
            self.expression += "**"
            self.text_input.set(self.expression)
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)
            
    def calculate(self):
        try:
            
            while self.expression.count('(') > self.expression.count(')'):
                self.expression += ')'
                
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = result
        except Exception as e:
            self.text_input.set("Error")
            self.expression = ""
            
    def delete_last(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)
        
    def clear_all(self):
        self.expression = ""
        self.text_input.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
