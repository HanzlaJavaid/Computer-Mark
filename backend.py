from tkinter import *

def convert(axis,mode,opcode,address):
    switcher = {
        "X":"0",
        "Y":"1",
        "D":"0",
        "I":"1",
        "LDA":"000",
        "ADD":"0001",
    }
    x = '{0:b}'.format(int(address))
    for i in range(0,10-len(x)):
        x = "0"+x
    print(switcher[axis]+switcher[mode]+switcher[opcode]+x) 
    return switcher[opcode]

def change_content(r,content):
    r['text'] = content.get(1.0, END+"-1c")
    print(content)

class MemoryWord():
    def __init__(self):
        self.wordsize = 16
        self.word = "0000000000000000"
    def __str__(self):
        return self.word

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
            opcode = convert(x[0],x[1])
            print(opcode)
        
        self.Print()