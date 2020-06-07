from tkinter import *
import os
def convert(axis,mode,opcode,address,indexer):
    switcher = {
        "X":"0",
        "Y":"1",
        "D":"0",
        "I":"1",
        "LDA":"0000",
        "ADD":"0001",
        "STO":"0010",
        "HLT":"1111",
    }
    a = indexer[address]
    x = '{0:b}'.format(int(a))
    for i in range(0,10-len(x)):
        x = "0"+x

    return(switcher[axis]+switcher[mode]+switcher[opcode]+x) 

def change_content(r,content):
    r['text'] = content


class Memory():

    def __init__(self):
        self.memorysize = 1024
        self.MEMORY = []
        self.REALMEMORY = []
        self.indexer = {}
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
        startIndex = len(self.indexer)
        insI = 0
        for i in range(startIndex,startIndex+len(temp)-1):
            x = temp[insI].split(' ')
            code = convert(x[0],x[1],x[2],x[3],self.indexer)
            real = x[0]+x[1]+x[2]+x[3]
            self.REALMEMORY[i] = real
            self.MEMORY[i] = code
            insI = insI+1
        self.Print()
    def ALLOCATE(self,r):
        raw = r.get(1.0,END)
        temp = raw.split('\n')
        for i in range(0,len(temp)-1):
            x = temp[i].split(':')
            self.indexer.update({x[0]:i})
            self.REALMEMORY[i] = int(x[1])
            j = '{0:b}'.format(int(x[1]))
            for k in range(0,16-len(j)):
                j = "0"+j
            self.MEMORY[i] = j
        self.Print()

class Register():
    def __init__(self,size,t):
        self.t = t
        self.output=None
        self.bits = size
        self.value=None
        self.outputVal="0000000000000000"
        if(t == "NUM"):
            self.value = int(0)
        if(t == "FULL"):
            self.value = "0000000000000000"
    
    def update(self):
        self.output['text'] = self.outputVal

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
        self.pc.value = 0;  
    
    def prepare(self):
        self.pc.value = len(self.memory.indexer)
        x = '{0:b}'.format(int(self.pc.value))
        for i in range(0,10-len(x)):
            x = "0"+x
        self.pc.outputVal = x
        self.pc.update()
    
    def ModifyOutput(self,val,outputsource):
        if outputsource.t == "FULL":
            if isinstance(val,str):
                a = val[0]
                b = val[1]
                c = val[2:5]
                d = val[5:]
                outputsource.outputVal = convert(a,b,c,d,self.memory.indexer)
            if isinstance(val,int):
                val = '{0:b}'.format(int(val))
                for i in range(0,16-len(val)):
                    val = "0"+val
                outputsource.outputVal = val
        if outputsource.t == "NUM":
            x = '{0:b}'.format(int(val))
            for i in range(0,outputsource.bits-len(x)):
                x = "0"+x
            outputsource.outputVal = x 
        outputsource.update()

    
    #Operations
    def DECODE(self,val): 
        value = self.memory.indexer[val[5:]]
        self.ar.value = int(value)
        if(val.find('LDA') != -1):
            return "LOAD_INSTRUCTION"
        if(val.find('ADD') != -1):
            return "ADD_INSTRUCTION"
        if(val.find('STO') != -1):
            return "STORE_INSTRUCTION"
        if(val.find('HLT') != -1):
            return "HALT"

    def RUN_PROGRAM(self):
        s = 1
        while(s == 1):
            s = self.FetchDecodeExecute()
        
    
    def FetchDecodeExecute(self):
        self.PC_TO_AR()
        self.INCREMENT_PC()
        self.Mar_TO_IR()
        print(self.ir.value)
        routine = self.DECODE(self.ir.value)
        if(routine == "LOAD_INSTRUCTION"):
            self.LOAD(self.ir.value[0],self.ir.value[1],self.ir.value[5:])
        if(routine == "ADD_INSTRUCTION"):
            self.ADD(self.ir.value[0],self.ir.value[1],self.ir.value[5:])
        if(routine == "STORE_INSTRUCTION"):
            self.STO(self.ir.value[0],self.ir.value[1],self.ir.value[5:])
            
        if(routine == "HALT"):
            return 0
        return 1

    def LOAD(self,axis,mode,address):
        self.Mar_TO_DR()
        if(axis == 'X'):
            self.DR_TO_XR()
        if(axis == 'Y'):
            self.DR_TO_YR()
    
    def ADD(self,axis,mode,address):
        self.Mar_TO_DR()
        if(axis == "X"):
            self.x.value = int(self.x.value) + int(self.dr.value)
        if(axis == "Y"):
            self.y.value = int(self.y.value) + int(self.dr.value)
        self.ModifyOutput(self.x.value,self.x)

    def STO(self,axis,mode,address):
         if(axis == "X"):
             self.XR_TO_Mar()

    #Microoperations
    def INCREMENT_PC(self):
        self.pc.value = self.pc.value + 1
        self.ModifyOutput(self.pc.value,self.pc)

    def PC_TO_AR(self):
        self.ar.value = self.pc.value
        self.ModifyOutput(self.ar.value,self.ar)

    def Mar_TO_IR(self):
        self.ir.value = self.memory.REALMEMORY[self.ar.value]
        self.ModifyOutput(self.ir.value,self.ir)

    def Mar_TO_DR(self):
        self.dr.value = self.memory.REALMEMORY[self.ar.value]
        self.ModifyOutput(self.dr.value,self.dr)
    
    def DR_TO_XR(self):
        self.x.value = self.dr.value
        self.ModifyOutput(self.x.value,self.x)

    def DR_TO_YR(self):
        self.y.value = self.dr.value
        self.ModifyOutput(self.y.value,self.y)
    
    def XR_TO_Mar(self):
        self.memory.REALMEMORY[self.ar.value] = self.x.value
        x = '{0:b}'.format(int(self.x.value))
        for i in range(0,16-len(x)):
            x = "0"+x
        self.memory.MEMORY[self.ar.value] = x
        self.memory.Print()
    def YR_TO_Mar(self):
        self.memory.REALMEMORY[self.ar.value] = self.y.value
        x = '{0:b}'.format(int(self.y.value))
        for i in range(0,16-len(x)):
            x = "0"+x
        self.memory.MEMORY[self.ar.value] = x
        self.memory.Print()
        


architecture = Architecture(acx,acy,pc,ar,ir,dr,inpr,outr,memory)
