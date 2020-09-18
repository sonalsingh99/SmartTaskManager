from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
import tkinter as tk
import sys
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

        lbl = Label(self, text="Smart Task Manager ")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = tk.Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)

        def printOutput():

            pl = PrintLogger(area)

    # replace sys.stdout with our object
            sys.stdout = pl

            self.after(10, do_something)

        abtn = Button(self, text="Apps",command=printOutput)
        abtn.grid(row=1, column=3)
    

        cbtn = Button(self, text="CPU-Graph")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Auto-Refresh")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="MODE",command=self.master.destroy)
        obtn.grid(row=5, column=3)
        self.quit =Button(self, text="QUIT",command=self.master.destroy)


       
def main():

    root = tk.Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':


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