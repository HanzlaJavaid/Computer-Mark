from tkinter import *

def convert(axis,mode,opcode,address):
    switcher = {
        "X":"0",
        "Y":"1",
        "D":"0",
        "I":"1",
        "LDA":"0000",
        "ADD":"0001",
        "HLT":"1111",
    }
    x = '{0:b}'.format(int(address))
    for i in range(0,10-len(x)):
        x = "0"+x

    return(switcher[axis]+switcher[mode]+switcher[opcode]+x) 

def change_content(r,content):
    r['text'] = content.get(1.0, END+"-1c")
    print(content)

class Memory():

    def __init__(self):
        self.memorysize = 1024
        self.MEMORY = []
        self.REALMEMORY = []
        self.output= None
        for i in range(0,self.memorysize):
            WORD = "0000000000000000"
            self.MEMORY.append(WORD)
            self.REALMEMORY.append("")
    def Print(self):
        if(self.output != None):
            self.output.delete('1.0', END)
            for i in range(0,self.memorysize):
                self.output.insert(END,self.MEMORY[i]+"\n")
    def LOAD(self,r):
        #Preprocessing Raw string
        raw = r.get(1.0,END)
        temp = raw.split('\n')
        for i in range(0,len(temp)-1):
            x = temp[i].split(' ')
            code = convert(x[0],x[1],x[2],x[3])
            real = x[0]+x[1]+x[2]+x[3]
            self.REALMEMORY[i] = real
            self.MEMORY[i] = code
        
        self.Print()

class Register():
    def __init__(self,size,t):
        self.output=None
        self.bits = size
        self.value=None
        self.outputVal="0000000000000000"
        if(t == "NUM"):
            self.value = int(0)
        if(t == "FULL"):
            self.value = "0000000000000000"

acx = Register(16,"NUM")
acy = Register(16,"NUM")
pc = Register(10,"NUM")
ar = Register(10,"NUM")
ir = Register(10,"FULL")
dr = Register(16,"NUM")
inpr = Register(10,"NUM")
outr = Register(10,"NUM")
memory = Memory()

class Architecture():
    def __init__(self,acx,acy,pc,ar,ir,dr,inpr,outr,memory):
        self.x = acx
        self.y = acy
        self.pc = pc
        self.ir = ir
        self.ar = ar
        self.dr = dr
        self.inpr = inpr
        self.outr = outr
        self.memory = memory  
    
    def ModifyOutput(self,val,outputsource):
        temp = val.split(' ')
        outputsource.outputVal = convert(temp[0],temp[1],temp[2],temp[3])
    
    #Operations
    def DECODE(self,val):
        if(val.find('LDA') != -1):
            return "LOAD_INSTRUCTION"

    def RUN_PROGRAM(self):
        for instrucion in self.memory.REALMEMORY:
            self.PC_TO_AR()
            self.INCREMENT_PC()
            self.Mar_TO_IR(self.ar.value)
            routine = self.DECODE(self.ir.value)
            print(self.ir.value)
            if(routine == "LOAD_INSTRUCTION"):
                self.LOAD()


    def LOAD(self,axis,mode,address):
        print("This is LDA")

    #Microoperations
    def INCREMENT_PC(self):
        self.pc.value = self.pc.value + 1
        self.pc.outputVal = '{0:b}'.format(int(self.pc.value))

    def PC_TO_AR(self):
        self.ar.value = self.pc.value
        #self.ModifyOutput(self.ar.value,self.ar)

    def Mar_TO_IR(self,mar):
        self.ir.value = self.memory.REALMEMORY[mar]
        #self.ModifyOutput(self.ir.value,self.ir)

architecture = Architecture(acx,acy,pc,ar,ir,dr,inpr,outr,memory)
