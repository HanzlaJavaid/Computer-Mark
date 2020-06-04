from tkinter import *

ROOT = Tk()

l1 = Label(ROOT, text="Assembly Code")
l1.pack()

CodeArea = Text()
CodeArea.grid(row = 1,column =1)


ROOT.mainloop()
