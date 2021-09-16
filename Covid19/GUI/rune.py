import tkinter as tk
from tkinter import mainloop, ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tall_a_label = tk.Label(self, text='Tall a')
        self.tall_a_label.pack(side="top")
        self.tall_a = tk.Entry(self)
        self.tall_a.pack(side="top")
        self.operator_select = ttk.Combobox(self)
        self.operator_select['values'] = ['+', '-', '*', '/']
        self.operator_select.pack(side="top")
        self.tall_b_label = tk.Label(self, text='Tall b')
        self.tall_b_label.pack(side="top")
        self.tall_b = tk.Entry(self)
        self.tall_b.pack(side="top")
        self.calc_button = tk.Button(self)
        self.calc_button["text"] = " = "
        self.calc_button["command"] = self.calc
        self.calc_button.pack(side="top")
        self.tall_c_label = tk.Label(self, text='Svaret vises her')
        self.tall_c_label.pack(side="top")
        self.quit = tk.Button(self, text="AVSLUTT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def calc(self):
        op = self.operator_select.get()
        c = Calculator(int(self.tall_a.get()), int(self.tall_b.get()))
        if op == '+': 
            self.tall_c_label['text'] = c.add()
        elif op == '-':
            self.tall_c_label['text'] = c.sub()
        elif op == '*':
            self.tall_c_label['text'] = c.mult()
        elif op == '/':
            self.tall_c_label['text'] = c.div()
        else:
            self.tall_c_label['text'] = 'Velg en operator'

class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def add(self):
        return self.a + self.b 
    
    def sub(self):
        return self.a - self.b 
    def mult(self):
        return self.a * self.b 
    def div(self):
        if self.b != 0:
            return self.a / self.b 
        else:
            return 'Dele på null!'
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Kalkulator')
    app = Application(master=root)
    app.mainloop()