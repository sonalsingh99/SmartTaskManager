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
        btn.config(image=offImg, bg="#CECCBE", activebackground="#CECCBE")
        root.config(bg="#CECCBE")
        
        btnState = False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="#2B2B2B")
       
        btnState = True

# loading the switch images:
onImg = PhotoImage(file =r"C:\Users\sonal\Downloads\sun.png")
offImg = PhotoImage(file =r"C:\Users\sonal\Downloads\sun-dark.png")


lbl = Label(root, text="Smart Task Manager ")
lbl.grid(sticky=W, pady=4, padx=5)

area = Text(root)
area.grid(row=1, column=0, columnspan=2, rowspan=4,
padx=5, sticky=E+W+S+N)

abtn = Button(root, text="Apps")
abtn.grid(row=1, column=3)
    

cbtn = Button(root, text="CPU-Graph")
cbtn.grid(row=2, column=3, pady=4)

hbtn = Button(root, text="Auto-Refresh")
hbtn.grid(row=5, column=0, padx=5)
# Night mode label:


# switch widget:
btn = tk.Button(root, text="OFF", borderwidth=0, command=switch, bg="#CECCBE", activebackground="#CECCBE")
btn.grid(row=5, column=3)
btn.config(image=offImg)

# window in mainloop:
root.mainloop()
    