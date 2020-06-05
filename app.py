from tkinter import *
from functools import partial
import backend
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
PC = Label(ROOT)
PC.grid(row = 1,column = 2)


l4 = Label(ROOT,text = "Instruction Register(IR): ")
l4.grid(row = 2,column = 1)
IR = Label(ROOT)
IR.grid(row = 2,column =2)


l5 = Label(ROOT,text = "X Register(XR): ")
l5.grid(row = 3,column = 1)
XR = Label(ROOT)
XR.grid(row = 3,column =2)

l6 = Label(ROOT,text = "Y Register(YR): ")
l6.grid(row = 4,column = 1)
YR = Label(ROOT)
YR.grid(row = 4,column =2)

l7 = Label(ROOT,text = "Data Register(DR): ")
l7.grid(row = 5,column = 1)
DR = Label(ROOT)
DR.grid(row = 5,column =2)

l8 = Label(ROOT,text = "INPR: ")
l8.grid(row = 6,column = 1)
INPR = Label(ROOT)
INPR.grid(row = 6,column =2)

l9 = Label(ROOT,text = "OUTR: ")
l9.grid(row = 7,column = 1)
OUTR = Label(ROOT)
OUTR.grid(row = 7,column =2)

l11 = Label(ROOT,text = "Address Register(AR): ")
l11.grid(row = 8,column =1)
AR = Label(ROOT)
AR.grid(row = 8,column =2)

l10 = Label(ROOT,text="Memory")
l10.grid(row = 0,column = 3,columnspan = 3)
RAM = Text(ROOT,width = 30, height =20)
RAM.grid(row = 1,column =3,rowspan = 8,columnspan =3)

backend.architecture.memory.output = RAM
backend.architecture.x.output = XR
backend.architecture.y.output = YR
backend.architecture.dr.output = DR
backend.architecture.inpr.output = INPR
backend.architecture.outr.output = OUTR
backend.architecture.ir.output = IR
backend.architecture.ar.output = AR
backend.architecture.pc.output = PC
#Connecting frontend with Backend
b1 = Button(ROOT,text = "Run Program",command = partial(backend.architecture.RUN_PROGRAM))
b1.grid(row = 9,column =0)
b2 = Button(ROOT,text = "Load Program",command = partial(backend.architecture.memory.LOAD,CodeArea))
b2.grid(row = 9,column =3,columnspan=3)



ROOT.mainloop()
