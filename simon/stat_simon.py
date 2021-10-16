import tkinter as tk

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

def write_high_score(window,max_seq,ent_name,new_high_scoreWindow,image_high_score):
    playerName=ent_name.get()
    with open('highScore.txt','w') as f:
        f.write(playerName+'\t'+str(max_seq)+'\n')
    new_high_scoreWindow.destroy()
    window.after(1000,show_high_score,image_high_score)

def new_high_score(window,max_seq,image_high_score):
    new_high_scoreWindow=tk.Toplevel()
    new_high_scoreWindow.title("New high score")
    ent_name=tk.Entry(new_high_scoreWindow)
    ent_name.insert(0,'Player')
    ent_name.pack(side=tk.BOTTOM)
    lbl_enter_name=tk.Label(new_high_scoreWindow,text="Enter your name",fg="black")
    lbl_enter_name.pack(side=tk.TOP)
    btn_enter_name=tk.Button(new_high_scoreWindow,text="Enter",
                             command=lambda:write_high_score(window,max_seq,ent_name,new_high_scoreWindow,image_high_score))
    btn_enter_name.pack(side=tk.BOTTOM)
    new_high_scoreWindow.mainloop()
    

def check_highScores(window,max_seq,image_high_score):
    highScore=read_high_score()
    if max_seq>highScore:
        new_high_score(window,max_seq,image_high_score)



