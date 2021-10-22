#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:19:28 2021

https://stackoverflow.com/questions/30690365/python-3-tkinter-button-command-inside-different-class
"""

import tkinter as tk
from time import sleep
from random import choice
from widget_simon import Widgets
from help_simon import printRules,about
from stat_simon import show_high_score,check_highScores

colors=["tomato2","yellow2","royal blue","lime green"]
correspondingColors=["red2","gold2","navy","green2"]
instructions=["Click on Play to launch the sequence",
              "Simon sequence","Reproduce the sequence",
              "Click on New Game to start a new game"]

def check(seq1,seq2):
    for col1,col2 in zip(seq1,seq2):
        if col1 != col2:
            return False
    return True

class Simon(tk.Frame):
    def __init__(self,parent, seqLg = 1,can_play=True):
        tk.Frame.__init__(self, parent)
        self.parent = parent
     
        self.seqLg = seqLg
        self.seqColors=[]
        self.can_play=can_play
    
    def current_seqLg(self):
        return self.seqLg
    
    def increment_seqLg(self):
        self.seqLg += 1
        self.can_play = True
    
    def reset_seqLg(self):
        self.seqLg = 1
        self.can_play = True

    def combination(self):
        idCol=[count for count in range(4)]
        self.seqColors=[choice(idCol) for i in range(self.seqLg)]
        self.can_play = False
    
    def get_seqColors(self):
        return self.seqColors

class Player(tk.Frame):
    def __init__(self,parent,can_play = False):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.can_play=can_play
        self.prop=[]
    
    def reset(self):
        self.prop=[]
        self.can_play = False
    
    def add_elm(self,elm):
        self.prop.append(elm)
        
    def get_current(self):
        return self.prop
       


class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def highlightButton(self,x):
        self.widgets.btn_Colors[x].configure(bg=correspondingColors[x])
        
    
    def resetButton(self,x):
        self.widgets.btn_Colors[x].configure(bg=colors[x])
        
    def flashButton(self,x):
        sleep(1)
        self.highlightButton(x)
        tk.Frame.update(self)
        sleep(1)
        self.resetButton(x)
        tk.Frame.update(self)  
    
    def playSequence(self,seqColors):
        seqColors=self.simon.seqColors
        for count in seqColors:
            idCol=count
            self.flashButton(idCol)
    
    def playSimon(self):
        if self.simon.can_play:
            self.widgets.lbl_instructions.configure(text=instructions[1])
            self.simon.combination()
            self.playSequence(self.simon.seqColors)
            self.player.can_play = True
            self.widgets.lbl_instructions.configure(text=instructions[2])
        
    def actionPlayer(self,x):
        if self.player.can_play and len(self.player.prop)<self.simon.current_seqLg():
            self.player.prop.append(x)
            seq=self.player.get_current()
        if len(self.player.prop)==self.simon.current_seqLg():
            self.player.reset()
            if check(seq,self.simon.get_seqColors()):
                self.widgets.lbl_instructions.configure(text=instructions[0])
                self.widgets.lbl_status.configure(text="   SUCCESS = "+str(self.simon.current_seqLg()))
                self.simon.increment_seqLg()
            else:
                max_seq=self.simon.current_seqLg()-1
                self.widgets.lbl_status.configure(text="   GAME OVER ! MAX= "+str(max_seq))
                check_highScores(max_seq)
                self.widgets.lbl_instructions.configure(text=instructions[-1])
                
    def new_game(self):
        self.simon.reset_seqLg()
        self.player.reset()
        self.widgets.lbl_instructions.configure(text=instructions[0])
        self.widgets.lbl_status.configure(text="   SUCCESS = 0")

    def initUI(self):

        self.parent.title("Simon game")

        self.pack()

        self.widgets = Widgets(self)
        self.widgets.pack(side="top", anchor="center", fill="both", expand=True)
        self.simon = Simon(self)
        self.player = Player(self)


def main():
    root = tk.Tk()
    App(root).pack(side="top", fill="both", expand=True)
    name='highScore.gif'
    image_high_score=tk.PhotoImage(file=name)
    top = tk.Menu(root)
    root.config(menu=top)
    helpMenu = tk.Menu(top, tearoff=False)
    
    top.add_command(label='Exit', command=root.destroy)
    top.add_command(label='Scores',command=lambda:show_high_score(image_high_score))
    top.add_cascade(label='Help', menu=helpMenu)
    
    helpMenu.add_command(label='How to play?',command=printRules)
    helpMenu.add_command(label='About',command=about)
    root.resizable(0,0)
    root.mainloop()

if __name__ == "__main__":
    main()
