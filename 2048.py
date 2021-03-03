# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 08:40:46 2021

@author: Chunky (oray-byte)
"""

import tkinter as tkr
import tkinter.messagebox as tkrm
import tkinter.font as tkrf
from typing import List, Tuple

class Game(tkr.Frame):
    
    def __init__(self, master=None):
        self.master = master
        super().__init__(master)
        self.master.geometry("600x600")
        tkr.Frame.pack(self)
        self.init_window()
        
    def init_window(self):
        canvas = tkr.Canvas(self.master, bg="gray34")
        
        canvas.create_rectangle(50, 50, 50, 50, fill="blue", outline="white")
        
        canvas.pack(side=tkr.TOP, expand=tkr.TRUE, fill=tkr.BOTH)
    
master = tkr.Tk()
game = Game(master)
master.mainloop()   