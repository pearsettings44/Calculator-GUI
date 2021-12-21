import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

SMALL_FONT_STYLE = ("Arial", 20)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)


class Calculator():
    """
    A class to represent a calculator.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the calculator object.
        """
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title = ("Calculator")

        self.result_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.result_label, self.current_label = self.create_display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,1)
        }

        self.operations = { "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            # Expand rows and collums to fit the window
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        """
        Used to create the "=" and "C" buttons.
        """
        self.create_clear_button()
        self.create_equal_button()

    def create_display_labels(self):
        """
        Creates two labels, one for the result expression and one for the ongoing expression.
        """
        result_label = tk.Label(self.display_frame, text=self.result_expression,
            anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        result_label.pack(expand=True, fill="both")

        current_label = tk.Label(self.display_frame, text=self.current_expression,
            anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill="both")

        return result_label, current_label

    def create_display_frame(self):
        """
        Creates the display frame.
        """
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        """
        Adds value to current expression.
        """
        self.current_expression += str(value)
        self.update_current_label()

    def create_digits_buttons(self):
        """
        Creates the digits (1,...,9) buttons.
        """
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE,
                            fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0,
                            command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        """
        Adds the operator
        """
        self.current_expression += operator
        self.result_expression += self.current_expression
        self.current_expression = ""
        self.update_current_label()
        self.update_result_label()

    def create_operator_buttons(self):
        """
        Creates the operators (/, *, +, -) buttons.
        """
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE,
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                            command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        """
        Clears the current and the result expressions.
        """
        self.current_expression = ""
        self.result_expression = ""
        self.update_result_label()
        self.update_current_label()

    def create_clear_button(self):
        """
        Creates the clear button.
        """
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE,
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                            command=self.clear)
        button.grid(row=0, column=1, columnspan=3 ,sticky=tk.NSEW)

    def evalute(self):
        """
        Uses eval to get the result.
        """
        self.result_expression += self.current_expression
        self.update_result_label

        self.current_expression = str(eval(self.result_expression))
        self.result_expression = ""
        self.update_current_label()

    def create_equal_button(self):
        """
        Creates the equal button
        """
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE,
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                            command=self.evalute)
        button.grid(row=4, column=3, columnspan=2 ,sticky=tk.NSEW)

    def create_buttons_frame(self):
        """
        Creates the buttons frame.
        """
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_result_label(self):
        """
        Updates the result label
        """
        self.result_label.config(text=self.result_expression)

    def update_current_label(self):
        """
        Updates the current label
        """
        self.current_label.config(text=self.current_expression)

    def run(self):
        """
        Tkinter mainloop utility.
        """
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
