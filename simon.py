from random import choice
import tkinter as tk
from time import sleep

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
            check_highScores(max_seq)
            
        
def check(seq1,seq2):
    for col1,col2 in zip(seq1,seq2):
        if col1 != col2:
            return False
    return True


def newGame(lbl_instructions,lbl_status,simon):
    simon.reset_seqLg()
    lbl_status.configure(text="   SUCCESS = "+str(simon.current_seqLg()-1))
    lbl_instructions.configure(text=instructions[0])


####################################################################################
def printRules():
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play?")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lbl_rules=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lbl_rules.pack(side=tk.TOP)
    ruleWindow.mainloop()


def about():
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.mainloop()

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

def show_high_score(image_high_score):
    high_scoreWindow=tk.Toplevel()
    high_scoreWindow.title("High score")
    with open('highScore.txt') as f:
        score_recovery=f.read()
    lbl_image=tk.Label(master=high_scoreWindow,image=image_high_score)
    lbl_image.pack()
    lbl_score_recovery=tk.Label(high_scoreWindow,text=score_recovery,fg="black",font='Arial 22')
    lbl_score_recovery.pack(side=tk.TOP)
    high_scoreWindow.mainloop() 

def write_high_score(max_seq,ent_name,new_high_scoreWindow):
    playerName=ent_name.get()
    with open('highScore.txt','w') as f:
        f.write(playerName+'\t'+str(max_seq)+'\n')
    new_high_scoreWindow.destroy()
    window.after(1000,show_high_score,image_high_score)

def new_high_score(max_seq):
    new_high_scoreWindow=tk.Toplevel()
    new_high_scoreWindow.title("New high score")
    ent_name=tk.Entry(new_high_scoreWindow)
    ent_name.insert(0,'Player')
    ent_name.pack(side=tk.BOTTOM)
    lbl_enter_name=tk.Label(new_high_scoreWindow,text="Enter your name",fg="black")
    lbl_enter_name.pack(side=tk.TOP)
    btn_enter_name=tk.Button(new_high_scoreWindow,text="Enter",
                             command=lambda:write_high_score(max_seq,ent_name,new_high_scoreWindow))
    btn_enter_name.pack(side=tk.BOTTOM)
    new_high_scoreWindow.mainloop()
    

def check_highScores(max_seq):
    highScore=read_high_score()
    if max_seq>highScore:
        new_high_score(max_seq)

############################################################################ 

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

