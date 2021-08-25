import random
import tkinter as tk
from time import sleep

colors=["tomato2","yellow2","royal blue","lime green"]
correspondingColors=["red2","gold2","navy","green2"]
seqColors=[]
lgSeq=1
can_play=False
player_prop=[]
instructions=["Click on Play to launch the sequence","Simon sequence","Reproduce the sequence"]


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
    global idCol,can_play,player_prop,lgSeq,lbl_status,max_seq
    idCol=x
    if can_play:
        player_prop.append(x)
        if len(player_prop)==lgSeq:
            if check():
                lbl_status.configure(text="   SUCCESS = "+str(lgSeq))
                lgSeq+=1
            else:
                max_seq=lgSeq-1
                lbl_status.configure(text="   GAME OVER ! MAX= "+str(max_seq))
                lgSeq=1
                check_highScores()
            window.after(1000,reinit)
        

def reinit():
    global can_play,player_prop,lbl_instructions,lbl_status
    can_play=False
    player_prop=[]
    lbl_instructions.configure(text=instructions[0])
    lbl_status.configure(text="   CURRENT NUMBER = "+str(lgSeq))
    

def check():
    for col1,col2 in zip(seqColors,player_prop):
        if col1 != col2:
            return False
    return True


def game():
    global lgSeq,success,can_play,lbl_instructions
    if not can_play:
        lbl_instructions.configure(text=instructions[1])
        combination()
        playSeq()
        can_play=True
        lbl_instructions.configure(text=instructions[2])
        

def newGame():
    global lgSeq
    lgSeq=1
    reinit()


def printRules():
    ruleWindow=tk.Toplevel()
    ruleWindow.title("Simon rules")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lbl_rules=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lbl_rules.pack(side=tk.TOP)
    ruleWindow.mainloop()

############################################################################
# High score recovery
############################################################################   
def read_high_score():
    '''
    Loads the text document 'highScore.txt' used to recover the high score

    Returns
    -------
    current_high_score : integer
        current high score.

    '''
    with open('highScore.txt') as f:
        score_recovery=f.readlines()
    current_high_score=int(score_recovery[0].split()[-1])
    return current_high_score

def show_high_score():
    global image_high_score
    high_scoreWindow=tk.Toplevel()
    high_scoreWindow.title("High score")
    with open('highScore.txt') as f:
        score_recovery=f.read()
    lbl_image=tk.Label(master=high_scoreWindow,image=image_high_score)
    lbl_image.pack()
    lbl_score_recovery=tk.Label(high_scoreWindow,text=score_recovery,fg="black",font='Arial 22')
    lbl_score_recovery.pack(side=tk.TOP)
    high_scoreWindow.mainloop()  
    
def write_high_score():
    global new_high_scoreWindow
    playerName=ent_name.get()
    with open('highScore.txt','w') as f:
        f.write(playerName+'\t'+str(max_seq)+'\n')
    new_high_scoreWindow.destroy()
    window.after(1000,show_high_score)

def new_high_score():
    global ent_name,new_high_scoreWindow
    new_high_scoreWindow=tk.Tk()
    new_high_scoreWindow.title("New high score")
    frameStat=tk.Canvas(new_high_scoreWindow,bg='white',height=500,width=500)
    frameStat.pack()
    ent_name=tk.Entry(frameStat)
    ent_name.insert(0,'Player')
    ent_name.pack(side=tk.BOTTOM)
    lab_Stat=tk.Label(frameStat,text="Enter your name",fg="black")
    lab_Stat.pack(side=tk.TOP)
    but_Enter=tk.Button(frameStat,text="Enter",command=write_high_score)
    but_Enter.pack(side=tk.BOTTOM)
    new_high_scoreWindow.mainloop()
    

def check_highScores():
    global highScore
    if max_seq>highScore:
        new_high_score()
        
highScore=read_high_score()
#####################################################################################################
## Graphics interface
#####################################################################################################
window=tk.Tk()
window.title("Simon")
frame=tk.Frame(window)
frame.pack(side=tk.TOP)
can = tk.Canvas(window,bg='black',height=60,width=50)
can.pack(side=tk.TOP,padx=5,pady=5)
top = tk.Menu(window)
window.config(menu=top)
gameMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=gameMenu)
gameMenu.add_command(label='New game', command=newGame)
gameMenu.add_command(label='Exit', command=window.destroy)
top.add_command(label='Rules',command=printRules)
top.add_command(label='Scores',command=show_high_score)

lbl_instructions=tk.Label(frame,text=instructions[0],fg="black")
lbl_instructions.pack(side=tk.TOP)

butGame=tk.Button(window,text="Play",command=game)
butGame.pack(side=tk.LEFT)
lbl_status=tk.Label(window,text="   CURRENT NUMBER = "+str(lgSeq),fg="black")
lbl_status.pack(side=tk.LEFT)

but_Colors=[]
for count in range(len(colors)):
    color=colors[count]
    but_Colors.append(tk.Button(can,bg=color,fg="black",height = 15,width = 20,command=lambda x=count:action(x)))
    but_Colors[count].pack(side=tk.LEFT)

name='highScore.gif'
image_high_score=tk.PhotoImage(file=name)

window.mainloop()
