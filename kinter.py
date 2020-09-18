from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
import tkinter as tk
import sys
from tkinter import PhotoImage
from tkinter import *
class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): 
        pass


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Smart Task Manager")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        self.config(bg="#CECCBE")


        area = tk.Text(self,background ="#CECCBE")
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)

        pl = PrintLogger(area)

    # replace sys.stdout with our object
        sys.stdout = pl

        self.after(10, do_something)


        
        abtn = tk.Button(self, text="Apps",borderwidth = 1)
        abtn.grid(row=1, column=3)
    

        cbtn = tk.Button(self, text="CPU-Graph",borderwidth = 1)
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = tk.Button(self, text="Auto-Refresh",borderwidth = 1)
        hbtn.grid(row=5, column=0, padx=5)
        # setting switch function:
        def switch():
            global btnState
            if btnState:
                btn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
                abtn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
                cbtn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
                hbtn.config(bg="#CECCBE", activebackground="#CECCBE",fg="black")
                self.config(bg="#CECCBE")
                area.config(bg="#CECCBE",fg="black")
                btnState = False
            else:
                btn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="white")
                abtn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="white")
                cbtn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="white")
                hbtn.config( bg="#2B2B2B", activebackground="#2B2B2B",fg="white")
                self.config(bg="#2B2B2B")
                area.config(bg="#2B2B2B",fg="white")
                btnState = True
        btn = tk.Button(self, text="MODE", command=switch,borderwidth = 1, bg="#CECCBE", activebackground="#CECCBE")
        btn.grid(row=5, column=3)
        btn.config(bg="#CECCBE")
           
        self.quit =Button(self, text="QUIT",command=self.master.destroy)


       
def main():
   
    root = tk.Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':

    btnState = False
    def do_something():
      
        import wmi 
  
    # Initializing the wmi constructor 
        f = wmi.WMI() 
  
    # Printing the header for the later columns 
        print("pid   Process name") 
  
    # Iterating through all the running processes  
        for process in f.Win32_Process(): 
      
        # Displaying the P_ID and P_Name of the process 
            print(f"{process.ProcessId:<10} {process.Name}")

    
    main()
