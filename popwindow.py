import tkinter as tk
from tkinter import ttk

def popup_bonus(label):
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text=label)
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)