from tkinter import *
from tkinter import colorchooser
from functools import partial
import backend
bit_8 = "00000000"
bit_16 = "00000000000000"
bit_10 = "0000000000"
x_col = 'red'
y_col = 'green'
pc_col = 'grey'
ir_col = 'orange'
ar_col = 'grey'
dr_col = '#00FFE4'
io_col = 'grey'
back_col = '#082592'


ROOT = Tk()
ROOT.title("Computer Mark Simulation")
f1 = Frame(ROOT)
f1.configure(background = back_col)
f1.grid(row = 0,column =0,columnspan = 5)
f2 = Frame(ROOT)
f2.grid(row = 1, column =0)
l1 = Label(f1, text="Assembly Code",width = 35)
l1.grid(row = 0 ,column =0)

CodeArea = Text(f1,width = 30, height =20)
CodeArea.grid(row = 1,column =0,rowspan = 8)

l2 = Label(f1,text="Computer Registers",width = 35)
l2.grid(row = 0 ,column = 1,columnspan = 2)

l3 = Label(f1,text = "Program Counter(PC):   ",background = pc_col)
l3.grid(row = 1,column = 1)
PC = Label(f1,text = bit_10,background = pc_col)
PC.grid(row = 1,column = 2)

l11 = Label(f1,text = "Address Register(AR):     ",background=ar_col)
l11.grid(row = 2,column =1)
AR = Label(f1,text = bit_10,background=ar_col)
AR.grid(row = 2,column =2)


l4 = Label(f1,text = "Instruction Register(IR): ",background = ir_col)
l4.grid(row = 3,column = 1)
IR = Label(f1,text = bit_16,background = ir_col)
IR.grid(row = 3,column =2)


l5 = Label(f1,text = "X Register(XR):                ",background = x_col)
l5.grid(row = 4,column = 1)
XR = Label(f1,background = x_col,text = bit_16)
XR.grid(row = 4,column =2)

l6 = Label(f1,text = "Y Register(YR):                ",background = y_col)
l6.grid(row = 5,column = 1)
YR = Label(f1,background = y_col,text = bit_16)
YR.grid(row = 5,column =2)

l7 = Label(f1,text = "Data Register(DR):          ",background = dr_col)
l7.grid(row = 6,column = 1)
DR = Label(f1,text = bit_16,background = dr_col)
DR.grid(row = 6,column =2)

l8 = Label(f1,text = "INPR: ",background = io_col)
l8.grid(row = 7,column = 1)
INPR = Label(f1,text = bit_10,background = io_col)
INPR.grid(row = 7,column =2)

l9 = Label(f1,text = "OUTR: ",background = io_col)
l9.grid(row = 8,column = 1)
OUTR = Label(f1,text =bit_10,background = io_col)
OUTR.grid(row = 8,column =2)

l10 = Label(f1,text="Memory",width = 35)
l10.grid(row = 0,column = 3)
RAM = Text(f1,width = 30, height =20)
RAM.grid(row = 1,column =3,rowspan = 8)

l13 = Label(f1,text="Stack",width = 35)
l13.grid(row = 0,column = 4,columnspan =2)
STACK = Text(f1,width = 30, height =10)
STACK.grid(row = 1,column =4,rowspan = 4,columnspan = 2)

l14 = Label(f1,text = "Stack Pointer(SP):     ",background = io_col)
l14.grid(row = 6,column = 4)
SP = Label(f1,text =bit_10,background = io_col)
SP.grid(row = 6,column =5)

l15 = Label(f1,text = "Stack size:                  ",background = io_col)
l15.grid(row = 7,column = 4)
SZ = Entry(f1,width = 10)
SZ.grid(row = 7,column =5)



l12 = Label(f1,text = "Allocate Memory",width = 35)
l12.grid(row = 0, column = 6)
MEMORY_CODE = Text(f1,width = 30,height = 20)
MEMORY_CODE.grid(row = 1,column =6,rowspan = 8)


def LOAD(CodeArea):
    backend.architecture.memory.LOAD(CodeArea)
    backend.architecture.prepare()

backend.architecture.memory.SetMemory()
backend.architecture.memory.output = RAM
backend.architecture.memory.stackout = STACK
backend.architecture.x.output = XR
backend.architecture.y.output = YR
backend.architecture.dr.output = DR
backend.architecture.inpr.output = INPR
backend.architecture.outr.output = OUTR
backend.architecture.ir.output = IR
backend.architecture.ar.output = AR
backend.architecture.pc.output = PC
backend.architecture.sp.output = SP
MEMORY_CODE.delete('1.0',END)
CodeArea.delete('1.0',END)
STACK.delete('1.0', END)
RAM.delete('1.0', END)



#Connecting frontend with Backend
b1 = Button(f1,text = "STEP",command = partial(backend.architecture.FetchDecodeExecute))
b1.grid(row = 11,column =1,pady=10)
b3 = Button(f1,text = "RUN",command = partial(backend.architecture.RUN_PROGRAM))
b3.grid(row = 11,column =2)
b4 = Button(f1,text = "ALLOCATE",command = partial(backend.architecture.memory.ALLOCATE,MEMORY_CODE))
b4.grid(row = 11,column =6)
b2 = Button(f1,text = "LOAD PROGRAM",command = partial(LOAD,CodeArea))
b2.grid(row = 11,column =0)
b5 = Button(f1,text = "Assign",command = partial(backend.architecture.setStackSize,SZ))
b5.grid(row = 8,column =5)


ROOT.mainloop()
