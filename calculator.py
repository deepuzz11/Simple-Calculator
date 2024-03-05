import tkinter as tk
import math

def add_to_display(value):
    current = display.get()
    if current == "Error":
        display.set("")
    display.set(current + value)

def calculate():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception:
        display.set("Error")

def clear():
    display.set("")

def square_root():
    try:
        result = math.sqrt(eval(display.get()))
        display.set(result)
    except Exception:
        display.set("Error")

def power():
    try:
        result = eval(display.get()) ** 2
        display.set(result)
    except Exception:
        display.set("Error")

def sine():
    try:
        result = math.sin(math.radians(eval(display.get())))
        display.set(result)
    except Exception:
        display.set("Error")

def cosine():
    try:
        result = math.cos(math.radians(eval(display.get())))
        display.set(result)
    except Exception:
        display.set("Error")

def tangent():
    try:
        result = math.tan(math.radians(eval(display.get())))
        display.set(result)
    except Exception:
        display.set("Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x400")
root.configure(bg="#FFB6C1")  # Set background color to millennial pink

# Create entry widget for display
display = tk.StringVar()
entry = tk.Entry(root, textvariable=display, font=("Arial", 20), bd=5, insertwidth=4, width=18, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("√", 5, 0), ("x^2", 5, 1), ("sin", 5, 2), ("cos", 5, 3),
    ("tan", 6, 0), ("C", 6, 1)
]

for btn_text, row, col in buttons:
    btn = tk.Button(root, text=btn_text, font=("Arial", 14), padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Bind functions to buttons
btn_sqrt = tk.Button(root, text="√", font=("Arial", 14), padx=20, pady=20, command=square_root)
btn_sqrt.grid(row=5, column=0, padx=5, pady=5)

btn_power = tk.Button(root, text="x^2", font=("Arial", 14), padx=20, pady=20, command=power)
btn_power.grid(row=5, column=1, padx=5, pady=5)

btn_sin = tk.Button(root, text="sin", font=("Arial", 14), padx=20, pady=20, command=sine)
btn_sin.grid(row=5, column=2, padx=5, pady=5)

btn_cos = tk.Button(root, text="cos", font=("Arial", 14), padx=20, pady=20, command=cosine)
btn_cos.grid(row=5, column=3, padx=5, pady=5)

btn_tan = tk.Button(root, text="tan", font=("Arial", 14), padx=20, pady=20, command=tangent)
btn_tan.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

btn_clear = tk.Button(root, text="Clear", font=("Arial", 14), padx=20, pady=20, command=clear)
btn_clear.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
