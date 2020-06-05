from tkinter import *

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
        for i in range(0,self.memorysize):
            WORD =  "0000000000000000"
            self.MEMORY.append(WORD)