from random import choice
import tkinter as tk
from time import sleep
from stat_simon import show_high_score,check_highScores
from help_simon import printRules,about

colors=["tomato2","yellow2","royal blue","lime green"]
correspondingColors=["red2","gold2","navy","green2"]
instructions=["Click on Play to launch the sequence",
              "Simon sequence","Reproduce the sequence",
              "Click on Game to start a new game"]

class Simon(object):
    def __init__(self,seqLg = 1):
        self.seqLg = seqLg
        self.seqColors=[]
    
    def current_seqLg(self):
        return self.seqLg
    
    def increment_seqLg(self):
        self.seqLg += 1
    
    def reset_seqLg(self):
        self.seqLg = 1

    def combination(self):
        idCol=[count for count in range(4)]
        self.seqColors=[choice(idCol) for i in range(self.seqLg)]
    
    def get_seqColors(self):
        return self.seqColors
    

class Player(object):
    def __init__(self,can_play = False):
        self.can_play=can_play
        self.prop=[]
    
    def reset(self):
        self.prop=[]
    
    def add_elm(self,elm):
        self.prop.append(elm)
        
    def get_current(self):
        return self.prop


def highlightButton(x):
    btn_Colors[x].configure(bg=correspondingColors[x])
    
    
def resetButton(x):
    btn_Colors[x].configure(bg=colors[x])
    

def flashButton(x,can):
    sleep(1)
    highlightButton(x)
    can.update()
    sleep(1)
    resetButton(x)
    can.update()    
    

def playSeq(can,lbl_instructions,simon,player):
    if not player.can_play:
        simon.combination()
        seqColors=simon.get_seqColors()
        lbl_instructions.configure(text=instructions[1])
        for count in seqColors:
            idCol=count
            flashButton(idCol,can)
        player.can_play=True
        lbl_instructions.configure(text=instructions[2])


def action(x,lbl_instructions,lbl_status,simon,player):
    if player.can_play and len(player.prop)<simon.current_seqLg():
        player.prop.append(x)
        seq=player.get_current()
    if len(player.prop)==simon.current_seqLg():
        player.can_play=False
        player.reset()
        if check(seq,simon.get_seqColors()):
            lbl_instructions.configure(text=instructions[0])
            lbl_status.configure(text="   SUCCESS = "+str(simon.current_seqLg()))
            simon.increment_seqLg()
        else:
            max_seq=simon.current_seqLg()-1
            lbl_status.configure(text="   GAME OVER ! MAX= "+str(max_seq))
            lbl_instructions.configure(text=instructions[-1])
            check_highScores(window,max_seq,image_high_score)
            
        
def check(seq1,seq2):
    for col1,col2 in zip(seq1,seq2):
        if col1 != col2:
            return False
    return True


def newGame(lbl_instructions,lbl_status,simon):
    simon.reset_seqLg()
    lbl_status.configure(text="   SUCCESS = "+str(simon.current_seqLg()-1))
    lbl_instructions.configure(text=instructions[0])




simon=Simon()
player=Player()

window=tk.Tk()
window.title("Simon")
frame=tk.Frame(window)
frame.pack(side=tk.TOP)
can = tk.Canvas(window,bg='black',height=60,width=50)
can.pack(side=tk.TOP,padx=5,pady=5)


name='highScore.gif'
image_high_score=tk.PhotoImage(file=name)

lbl_instructions=tk.Label(frame,text=instructions[0],fg="black")
lbl_instructions.pack(side=tk.TOP)

butGame=tk.Button(window,text="Play",command=lambda :playSeq(can,lbl_instructions,simon,player))
butGame.pack(side=tk.LEFT) 

lbl_status=tk.Label(window,text="   SUCCESS = "+str(simon.current_seqLg()-1),fg="black")
lbl_status.pack(side=tk.LEFT)

btn_Colors=[]
for count in range(len(colors)):
    color=colors[count]
    btn_Colors.append(tk.Button(can,bg=color,fg="black",height = 15,width = 20,
                                command=lambda x=count:action(x,lbl_instructions,lbl_status,simon,player)))
    btn_Colors[count].pack(side=tk.LEFT)


#Menu
top = tk.Menu(window)
window.config(menu=top)
gameMenu = tk.Menu(top, tearoff=False)
helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=gameMenu)
gameMenu.add_command(label='New game', command=lambda:newGame(lbl_instructions,lbl_status,simon))
gameMenu.add_command(label='Exit', command=window.destroy)
top.add_command(label='Scores',command=lambda:show_high_score(image_high_score))
top.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='How to play?',command=printRules)
helpMenu.add_command(label='About',command=about)
window.mainloop()

