import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            result_label.config(text="Invalid operation")
            return

        result_label.config(text=f"Answer: {result}")
        again_button.config(state="normal")

    except ValueError:
        result_label.config(text="Invalid input")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation.set("+")
    result_label.config(text="")
    again_button.config(state="disabled")
    messagebox.showinfo("No More Free Trial", "no more free tryal 😅")

# Setup window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.configure(bg="cyan")

# First number
tk.Label(root, text="First Number:", bg="cyan", font=("Arial", 12)).pack()
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack()

# Operation
tk.Label(root, text="Operation (+, -, *, /):", bg="cyan", font=("Arial", 12)).pack()
operation = tk.StringVar(value="+")
op_menu = tk.OptionMenu(root, operation, "+", "-", "*", "/")
op_menu.pack()

# Second number
tk.Label(root, text="Second Number:", bg="cyan", font=("Arial", 12)).pack()
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12)).pack(pady=10)

# Result display
result_label = tk.Label(root, text="", bg="cyan", font=("Arial", 16))
result_label.pack()

# Go again button
again_button = tk.Button(root, text="Go Again", command=reset, state="disabled", font=("Arial", 12))
again_button.pack(pady=5)

root.mainloop()
