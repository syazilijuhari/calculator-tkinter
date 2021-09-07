from tkinter import *
import tkinter as tk

large_font_style = ("Arial", 40, "bold")
small_font_style = ("Arial", 16)
digit_font_style = ("Arial", 24, "bold")
default_font_style = ("Arial", 20)

display_color = "#1A237E"
label_color = "#E8EAF6"
button_color = "#303F9F"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()

        self.operation = {"/" : "\u00F7", "*" : "\u00D7", "-" : "-", "+" : "+"}
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1), 0:(4,2)
        }

        self.button_frame = self.create_button_frame()
        self.create_digit_button()
        self.create_operator_button()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()

        self.button_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=display_color, fg=label_color, padx=24, font=small_font_style)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=display_color, fg=label_color, padx=24, font=large_font_style)
        label.pack(expand=True, fill="both")
    
        return total_label, label 

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=display_color)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=button_color, fg=label_color, font=digit_font_style, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_button(self):
        i=0
        for operator, symbol in self.operation.items():
            button = tk.Button(self.button_frame, text=symbol, bg=button_color, fg=label_color, font=default_font_style, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=button_color, fg=label_color, font=default_font_style, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=button_color, fg=label_color, font=default_font_style, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label

    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=button_color, fg=label_color, font=default_font_style, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""

        except Exception as e:
             self.current_expression = "Error"

        finally:
            self.update_label()

    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=button_color, fg=label_color, font=default_font_style, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operation.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()
    
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()

