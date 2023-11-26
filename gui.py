import tkinter as tk
from tkinter import messagebox

def set_python_version(version):
    # Here you would add the logic to change the system's Python version
    messagebox.showinfo("Python Version Switcher", f"Switching to Python {version}")

app = tk.Tk()
app.title("Python Version Switcher")

tk.Button(app, text="Switch to Python 310", command=lambda: set_python_version("310")).pack()
tk.Button(app, text="Switch to Python 312", command=lambda: set_python_version("312")).pack()

app.mainloop()
