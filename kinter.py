import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style

# setting root window:
root = tk.Tk()
root.title("SMART TASK MANAGER")
root.columnconfigure(1, weight=1)
root.columnconfigure(3, pad=7)
root.rowconfigure(3, weight=1)
root.rowconfigure(5, pad=7)
root.config(bg="#CECCBE")
root.geometry("350x300+300+300")

# setting switch state:
btnState = False

# setting switch function:
def switch():
    global btnState
    if btnState:
        btn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
        abtn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
        cbtn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
        hbtn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
        root.config(bg="#CECCBE")
        area.config(bg="#CECCBE")
        btnState = False
    else:
        btn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="green")
        abtn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="green")
        cbtn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="green")
        hbtn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="green")
        root.config(bg="#2B2B2B")
        area.config(bg="#2B2B2B")
        btnState = True


area = tk.Text(root,background ="#CECCBE")
area.grid(row=1, column=0, columnspan=2, rowspan=4,
padx=5, sticky=E+W+S+N)

abtn = tk.Button(root, text="Apps",borderwidth = 1)
abtn.grid(row=1, column=3)
    

cbtn = tk.Button(root, text="CPU-Graph",borderwidth = 1)
cbtn.grid(row=2, column=3, pady=4)

hbtn = tk.Button(root, text="Auto-Refresh",borderwidth = 1)
hbtn.grid(row=5, column=0, padx=5)


# switch widget:
btn = tk.Button(root, text="Mode", command=switch,borderwidth = 1, bg="#CECCBE", activebackground="#CECCBE")
btn.grid(row=5, column=3)
btn.config(bg="#CECCBE")





# window in mainloop:
root.mainloop()
    