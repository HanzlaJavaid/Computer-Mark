from tkinter import *
WIDTH_FOR_REGISTEROUTPUT = 10

ROOT = Tk()

l1 = Label(ROOT, text="Assembly Code")
l1.grid(row = 0 ,column =0)

CodeArea = Text(ROOT,width = 30, height =20)
CodeArea.grid(row = 1,column =0,rowspan = 8)

l2 = Label(ROOT,text="Computer Registers")
l2.grid(row = 0 ,column = 1,columnspan = 2)

l3 = Label(ROOT,text = "Program Counter(PC): ")
l3.grid(row = 1,column = 1)
PC = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
PC.grid(row = 1,column = 2)


l4 = Label(ROOT,text = "Instruction Register(IR): ")
l4.grid(row = 2,column = 1)
IR = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
IR.grid(row = 2,column =2)


l5 = Label(ROOT,text = "X Register(XR): ")
l5.grid(row = 3,column = 1)
XR = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
XR.grid(row = 3,column =2)

l6 = Label(ROOT,text = "Y Register(YR): ")
l6.grid(row = 4,column = 1)
YR = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
YR.grid(row = 4,column =2)

l7 = Label(ROOT,text = "Data Register(DR): ")
l7.grid(row = 5,column = 1)
DR = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
DR.grid(row = 5,column =2)

l8 = Label(ROOT,text = "INPR: ")
l8.grid(row = 6,column = 1)
INPR = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
INPR.grid(row = 6,column =2)

l9 = Label(ROOT,text = "OUTR: ")
l9.grid(row = 7,column = 1)
OUTR = Text(ROOT,width=WIDTH_FOR_REGISTEROUTPUT,height=1)
OUTR.grid(row = 7,column =2)

b1 = Button(ROOT,text = "Run Program")
b1.grid(row = 9,column =0)
ROOT.mainloop()
