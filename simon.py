import random
import tkinter as tk
from time import sleep

colors=["tomato2","yellow2","royal blue","lime green"]
correspondingColors=["red2","gold2","navy","green2"]
seqColors=[]
lgSeq=1
can_play=False
player_prop=[]
messages=["Click on Play to launch the sequence","Simon sequence","Reproduce the sequence"]

def combination():
    global seqColors,lgSeq
    idCol=[count for count in range(4)]
    seqColors=[random.choice(idCol) for i in range(lgSeq)]
    
    
def actionButton(x):
    but_Colors[x].configure(bg=colors[x])
    

def highlightButton():
    global idCol
    x=idCol
    but_Colors[x].configure(bg=correspondingColors[x])
    
    
def resetButton():
    global idCol
    x=idCol
    but_Colors[x].configure(bg=colors[x])
    

def flashButton():
    global can
    sleep(1)
    highlightButton()
    can.update()
    sleep(1)
    resetButton()
    can.update()    
    

def playSeq():
    global idCol,seqColors,can
    for count in seqColors:
        idCol=count
        flashButton()
        
       
def action(x):
    global idCol,can_play,player_prop,lgSeq,lab_Message2
    idCol=x
    if can_play:
        player_prop.append(x)
        if len(player_prop)==lgSeq:
            if check():
                lab_Message2.configure(text="   SUCCESS = "+str(lgSeq))
                lgSeq+=1
            else:
                lab_Message2.configure(text="   GAME OVER ! MAX= "+str(lgSeq-1))
                lgSeq=1
            window.after(1000,reinit)
        

def reinit():
    global can_play,player_prop,lab_Message,lab_Message2
    can_play=False
    player_prop=[]
    lab_Message.configure(text=messages[0])
    lab_Message2.configure(text="   CURRENT NUMBER = "+str(lgSeq))
    

def check():
    for col1,col2 in zip(seqColors,player_prop):
        if col1 != col2:
            return False
    return True


def game():
    global lgSeq,success,can_play,lab_Message
    if not can_play:
        lab_Message.configure(text=messages[1])
        combination()
        playSeq()
        can_play=True
        lab_Message.configure(text=messages[2])
        

def newGame():
    global lgSeq
    lgSeq=1
    reinit()


def printRules():
    global ruleWindow
    ruleWindow=tk.Tk()
    ruleWindow.title("Simon rules")
    frameRule=tk.Canvas(ruleWindow,bg='white',height=500,width=500)
    frameRule.pack()  
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(frameRule,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()
#####################################################################################################
## Graphics interface
#####################################################################################################
window=tk.Tk()
window.title("Simon")
frame=tk.Frame(window)
frame.pack(side=tk.TOP)
can = tk.Canvas(window)
can.pack(side=tk.TOP,padx=5,pady=5)
top = tk.Menu(window)
window.config(menu=top)
gameMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=gameMenu)
gameMenu.add_command(label='New game', command=newGame)
gameMenu.add_command(label='Exit', command=window.destroy)
top.add_command(label='Rules',command=printRules)

lab_Message=tk.Label(frame,text=messages[0],fg="black")
lab_Message.pack(side=tk.TOP)

butGame=tk.Button(window,text="Play",command=game)
butGame.pack(side=tk.LEFT)
lab_Message2=tk.Label(window,text="   CURRENT NUMBER = "+str(lgSeq),fg="black")
lab_Message2.pack(side=tk.LEFT)

but_Colors=[]
for count in range(len(colors)):
    color=colors[count]
    but_Colors.append(tk.Button(can,bg=color,fg="black",height = 15,width = 20,command=lambda x=count:action(x)))
    but_Colors[count].pack(side=tk.LEFT)

window.mainloop()
