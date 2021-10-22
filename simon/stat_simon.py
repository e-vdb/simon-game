#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:09:51 2021

@author: Emeline
"""
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
    '''
    Opens a secondary window in the GUI which displays the current highest score.
    A Button allows the player to reset the high score.

    Parameters
    ----------
    image_high_score : PhotoImage object of tkinter module
        gif image illustrating the high score.

    Returns
    -------
    None.

    '''
    high_scoreWindow=tk.Toplevel()
    high_scoreWindow.title("High score")
    with open('highScore.txt') as f:
        score_recovery=f.read()
    lbl_image=tk.Label(master=high_scoreWindow,image=image_high_score)
    lbl_image.pack()
    lbl_score_recovery=tk.Label(high_scoreWindow,text=score_recovery,fg="black",font='Arial 22')
    lbl_score_recovery.pack(side=tk.TOP)
    btn_reset=tk.Button(master=high_scoreWindow,
                        text="Reset",fg="red",font='Arial 15',
                        command=lambda:reset_high_score(high_scoreWindow))
    btn_reset.pack()
    high_scoreWindow.resizable(0,0)
    high_scoreWindow.mainloop() 
    
    
def reset_high_score(high_scoreWindow):
    '''
    Erases the current high score and closes the window displaying the high score.

    Parameters
    ----------
    high_scoreWindow : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    playerName="Player"
    with open('highScore.txt','w') as f:
        f.write(playerName+'\t'+str(0)+'\n')
    high_scoreWindow.destroy()
    

def write_high_score(max_seq,ent_name,new_high_scoreWindow):
    '''
    Reads the player name from new_high_scoreWindow and closes this window.

    Parameters
    ----------
    max_seq : integer
        score performed by the player.
    ent_name : string
        player name extracted from the entry widget of new_high_scoreWindow.
    new_high_scoreWindow : tkinter window
        window where the player can enter his name.

    Returns
    -------
    None.

    '''
    playerName=ent_name.get()
    with open('highScore.txt','w') as f:
        f.write(playerName+'\t'+str(max_seq)+'\n')
    new_high_scoreWindow.destroy()


def new_high_score(max_seq):
    '''
    Opens a secondary window where the player enters his name.

    Parameters
    ----------
    max_seq : integer
        score performed by the player.

    Returns
    -------
    None.

    '''
    new_high_scoreWindow=tk.Toplevel()
    new_high_scoreWindow.title("New high score")
    lbl_text=tk.Label(new_high_scoreWindow,
                      text="Congratulations.\n You have the new high score",
                      fg="black",font='Arial 22')
    lbl_text.pack()
    lbl_score=tk.Label(new_high_scoreWindow,text=str(max_seq),fg="black",font='Arial 15')
    lbl_score.pack()
    lbl_enter_name=tk.Label(new_high_scoreWindow,text="Enter your name",fg="black")
    lbl_enter_name.pack()
    ent_name=tk.Entry(new_high_scoreWindow)
    ent_name.insert(0,'Player')
    ent_name.pack()
    btn_enter_name=tk.Button(new_high_scoreWindow,text="Enter",
                    command=lambda:write_high_score(max_seq,ent_name,new_high_scoreWindow))
    btn_enter_name.pack()
    new_high_scoreWindow.resizable(0,0)
    new_high_scoreWindow.mainloop()
    

def check_highScores(max_seq):
    '''
    Compares the score performed by the player with the high score.
    If it is larger, it saves the new high score.

    Parameters
    ----------
    max_seq : integer
        score performed by the player.

    Returns
    -------
    None.

    '''
    highScore=read_high_score()
    if max_seq>highScore:
        new_high_score(max_seq)