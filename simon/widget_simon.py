"""


"""
import tkinter as tk

colors=["tomato2","yellow2","royal blue","lime green"]
instructions=["Click on Play to launch the sequence",
              "Simon sequence","Reproduce the sequence",
              "Click on Game to start a new game"]
class Widgets(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self):

        self.lbl_instructions=tk.Label(text=instructions[0],fg="black")
        self.lbl_instructions.pack(side=tk.TOP)
        
        self.button = tk.Button(text='Play', command=self.parent.playSimon)
        self.button.pack(side=tk.TOP)
        self.lbl_status=tk.Label(text="  SUCCESS = 0",fg="black")
        self.lbl_status.pack(side=tk.TOP)
        
        self.btn_Colors=[]
        self.btn_new_game = tk.Button(text='New game', command=self.parent.new_game)
        self.btn_new_game.pack(side=tk.BOTTOM)
        
        for count in range(len(colors)):
            color=colors[count]
            self.btn_Colors.append(tk.Button(bg=color,fg="black",height = 15,width = 20,
                                             command=lambda x=count : self.parent.actionPlayer(x)))
                                             
            self.btn_Colors[count].pack(side=tk.LEFT)