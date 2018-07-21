import tkinter as tk
import calculator_functions
import math


window = tk.Tk()
window.resizable(0, 0)
window.title("Calculator")

# Top Row Frames
top_row = tk.Frame(window)
top_row.grid(row=0, column=0, columnspan=3, sticky="n")

# Use and Entry for editable display
display = tk.Entry(window, width=60, bg="powder blue", bd=20, relief="ridge")
display.grid(row=0, columnspan=3)

# Num Pad Frame
num_pad = tk.Frame(window)
num_pad.grid(row=1, column=0, sticky="n")

# Num Pad Keys
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '.', '0', ' , ',
    "=", "DEL"
]
r = 0
c = 0

for button in num_pad_list:
    def cmd(x=button):
        click(x)

    tk.Button(num_pad, text=button, width=7, command=cmd).grid(row=r, column=c)

    c += 1
    if c > 2:
        c = 0
        r += 1

# operators:
operator = tk.Frame(window)
operator.grid(row=1, column=1, sticky="e")

operator_list = [
    " * ", " C ", " / ",
    " + ", " - ",
    " ( ", " ) ",
    " √ ", " ∛ ",
    " x^2 ", " x^3 ",
    " ** ",
    " ln ", " log_10 ",
    " sin ", " cos ", " tan ",

    ]

r = 0
c = 0
for b in operator_list:
    def cmd(x=b):
        click(x)

    if b == " ** ":
        tk.Button(operator, text=" x^y ", width=5, command=cmd).grid(row=r, column=c)

    else:
        tk.Button(operator, text=b, width=5, command=cmd).grid(row=r, column=c)

    c += 1
    if c > 3:
        c = 0
        r += 1

# Constants
constants = tk.Frame(window)
constants.grid(row=3, column=0, sticky="nw")
constants_list = [
    "π",
    "e"
]

r = 0
c = 0
for b in constants_list:
    def cmd(x=b):
        click(x)

    tk.Button(constants, text=b, width=20, command=cmd).grid(row=r, column=c)
    r += 1

# Functions
functions = tk.Frame(window)
functions.grid(row=2, column=1, sticky="w")
functions_list = [
    "Factorial(!)",
    "-> Roman",
    "-> Binary",
    "Binary -> 10"
]

r = 0
c = 0
for b in functions_list:
    def cmd(x=b):
        click(x)

    tk.Button(functions, text=b, width=20, command=cmd).grid(row=r, column=c)
    r += 1


def click(key):

    if display.get() == "Error":
        display.delete(0, tk.END)
        display.insert(tk.END, key)

    elif key == "=":
        try:
            temp = display.get()
            resultchars = temp.split()

            for i in range(0, len(resultchars)):
                if (not(resultchars[i] == "+" or resultchars[i] == "-" or resultchars[i] == "*"
                        or resultchars[i] == "/" or resultchars[i] == "(" or resultchars[i] == ")"
                        or resultchars[i] == "√" or resultchars[i] == "**" or resultchars[i] == "√"
                        or resultchars[i] == "∛" or resultchars[i] == "ln" or resultchars[i] == "log_10"
                        or resultchars[i] == "sin" or resultchars[i] == "cos" or resultchars[i] == "tan"
                        )):
                    resultchars[i] = float(resultchars[i])
            temp = ""

            for i in range(0, len(resultchars)):
                temp = temp + str(resultchars[i])

            result = str(eval(temp))[0:15]
            display.delete(0, tk.END)
            display.insert(tk.END, result)

        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "-----> Syntax Error")

    elif key == " C ":
        display.delete(0, tk.END)

    elif key == constants_list[0]:
        display.insert(tk.END, math.pi)

    elif key == constants_list[1]:
        display.insert(tk.END, math.e)

    elif key == functions_list[0]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.factorial(n))

    elif key == functions_list[1]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.to_roman(n))

    elif key == functions_list[2]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.to_binary(n))

    elif key == functions_list[3]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.from_binary(n))

    elif key == operator_list[7]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.sqrt(n))

    elif key == operator_list[8]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.cube_root(n))

    elif key == operator_list[9]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.raised_to_2(n))

    elif key == operator_list[10]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.raised_to_3(n))

    elif key == operator_list[12]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.natural_log(n))

    elif key == operator_list[13]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.logarithm(n))

    elif key == operator_list[14]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.sine(n))

    elif key == operator_list[15]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.cosine(n))

    elif key == operator_list[16]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.tangent(n))

    elif key == num_pad_list[13]:
        n = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, calculator_functions.delete(n))

    else:
        display.insert(tk.END, key)

# MainLoop
window.mainloop()

