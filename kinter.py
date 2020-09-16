from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style


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

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="Apps")
        abtn.grid(row=1, column=3)
    

        cbtn = Button(self, text="CPU-Graph")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Auto-Refresh")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="MODE",command=self.master.destroy)
        obtn.grid(row=5, column=3)
        self.quit =Button(self, text="QUIT",command=self.master.destroy)
       
def main():

    root = Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()