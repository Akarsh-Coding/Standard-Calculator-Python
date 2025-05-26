from tkinter import *
from tkinter import ttk
from math import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Calculator")
        self.root.geometry("325x500")
        self.root.resizable(False, False)

        self.input = ""         # to store the user input
        self.bracket_count = 0  # Track opening/closing




        # Display
        self.dis = Entry(self.root,relief="solid",bd=3,justify="right",
                    font=("Agency FB", 30, "bold"),bg="#3F3F3F",fg="#84C17C")
        self.dis.place(x=7,y=70,width=310,height=70)


        # Separator
        s = ttk.Separator(self.root, orient="horizontal")
        s.place(x=12, y=145, width=300)

        # Button Frame
        button_frame = Frame(self.root, width=315, height=345, bg="#000000")
        button_frame.place(x=2, y=153)

        # Common Sizes
        btn_w = 7
        btn_h = 1
        font_regular = ("Agency FB", 20)
        font_number = ("Agency FB", 19, "bold")
        btn_numb_c = "#303030"
        btn_func_c = "#292828"
        font_numb_c = "#03EB03"
        font_func_c = "#13B513"

        # Row 0
        Button(button_frame, text="%", bd=0, relief="flat",
                width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c ,fg= font_func_c,
                command=self.percent
                ).grid(row=0, column=0, padx=2, pady=2)
        Button(button_frame, text="CE", bd=0, relief="flat",
                width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                command=self.clear_all
                ).grid(row=0, column=1, padx=2, pady=2)
        Button(button_frame, text="( )", bd=0, relief="flat", 
                width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                command=self.bracket
                ).grid(row=0, column=2, padx=2, pady=2)
        Button(button_frame, text="⇽", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=self.backspace
                    ).grid(row=0, column=3, padx=2, pady=2)

        # Row 1
        Button(button_frame, text="1/x", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=self.reciprocal
                    ).grid(row=1, column=0, padx=2, pady=2)
        Button(button_frame, text="x²", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=self.square
                    ).grid(row=1, column=1, padx=2, pady=2)
        Button(button_frame, text="√", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=self.sqrt
                    ).grid(row=1, column=2, padx=2, pady=2)
        Button(button_frame, text="÷", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=lambda: self.press("/")
                    ).grid(row=1, column=3, padx=2, pady=2)

        # Row 2
        Button(button_frame, text="7", bd=0,relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c,
                    command=lambda:self.press(7)
                    ).grid(row=2, column=0, padx=2, pady=2)
        Button(button_frame, text="8", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c,
                    command=lambda:self.press(8)
                    ).grid(row=2, column=1, padx=2, pady=2)
        Button(button_frame, text="9", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c, 
                    command=lambda:self.press(9)
                    ).grid(row=2, column=2, padx=2, pady=2)
        Button(button_frame, text="×", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=lambda: self.press('*')
                    ).grid(row=2, column=3, padx=2, pady=2)

        # Row 3
        Button(button_frame, text="4", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c,
                    command=lambda:self.press(4)
                    ).grid(row=3, column=0, padx=2, pady=2)
        Button(button_frame, text="5", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c,
                    command=lambda:self.press(5)
                    ).grid(row=3, column=1, padx=2, pady=2)
        Button(button_frame, text="6", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c,
                    command=lambda:self.press(6)
                    ).grid(row=3, column=2, padx=2, pady=2)
        Button(button_frame, text="–", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=lambda: self.press("-")
                    ).grid(row=3, column=3, padx=2, pady=2)

        # Row 4
        Button(button_frame, text="1", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c, 
                    command=lambda:self.press(1)
                    ).grid(row=4, column=0, padx=2, pady=2)
        Button(button_frame, text="2", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c, 
                    command=lambda:self.press(2)
                    ).grid(row=4, column=1, padx=2, pady=2)
        Button(button_frame, text="3", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c, 
                    command=lambda:self.press(3)
                    ).grid(row=4, column=2, padx=2, pady=2)
        Button(button_frame, text="+", bd=0, relief="flat", 
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=lambda: self.press("+")
                    ).grid(row=4, column=3, padx=2, pady=2)

        # Row 5
        Button(button_frame, text="±", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=self.toggle_sign).grid(row=5, column=0, padx=2, pady=2)
        Button(button_frame, text="0", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_number, bg=btn_numb_c, fg= font_numb_c,
                    command=lambda:self.press(0)
                    ).grid(row=5, column=1, padx=2, pady=2)
        Button(button_frame, text=".", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_regular, bg=btn_func_c, fg= font_func_c,
                    command=lambda:self.press(".")
                    ).grid(row=5, column=2, padx=2, pady=2)
        Button(button_frame, text="=", bd=0, relief="flat",
                    width=btn_w, height=btn_h, font=font_regular, bg= "#3FB920", fg= "#FFFFFF",
                    command=self.evaluate).grid(row=5, column=3, padx=2, pady=2)



    # Button Actions
    def press(self, value):
        self.input += str(value)
        self.dis.delete(0, END)
        self.dis.insert(END, self.input)

    def clear_all(self):
        self.input = ""
        self.dis.delete(0, END)

    def bracket(self):
        if self.bracket_count % 2 == 0:
            self.press("(")
        else:
            self.press(")")
        self.bracket_count += 1


    def backspace(self):
        self.input = self.input[:-1]
        self.dis.delete(0, END)
        self.dis.insert(END, self.input)

    def evaluate(self):
        try:
            result = str(eval(self.input))
            self.dis.delete(0, END)
            self.dis.insert(END, result)
            self.input = result
        except:
            self.dis.delete(0, END)
            self.dis.insert(END, "Error")
            self.input = ""

    def toggle_sign(self):
        if self.dis.get().startswith("-"):
            self.input = self.dis.get()[1:]
        else:
            self.input = "-" + self.dis.get()
        self.dis.delete(0, END)
        self.dis.insert(END, self.input)

    def percent(self):
        try:
            value = float(self.dis.get()) / 100
            self.input = str(value)
            self.dis.delete(0, END)
            self.dis.insert(END, self.input)
        except:
            pass

    def square(self):
        try:
            value = float(self.dis.get()) ** 2
            self.input = str(value)
            self.dis.delete(0, END)
            self.dis.insert(END, self.input)
        except:
            pass

    def sqrt(self):
        try:
            value = sqrt(float(self.dis.get()))
            self.input = str(value)
            self.dis.delete(0, END)
            self.dis.insert(END, self.input)
        except:
            pass

    def reciprocal(self):
        try:
            value = 1 / float(self.dis.get())
            self.input = str(value)
            self.dis.delete(0, END)
            self.dis.insert(END, self.input)
        except:
            pass


if __name__ == "__main__":
    root = Tk()
    root.config(bg="#000000")
    app = Calculator(root)
    root.mainloop()
