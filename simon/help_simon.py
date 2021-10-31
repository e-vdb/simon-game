#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:47:36 2021

@author: Emeline
"""
import tkinter as tk

def printRules():
    """
    Load the text document rules_eng.txt.
    Open a secondary window to display the rules.

    Returns
    -------
    None.

    """
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play?")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lbl_rules=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lbl_rules.pack(side=tk.TOP)
    ruleWindow.resizable(0,0)
    ruleWindow.mainloop()


def about():
    """
    Load the text document about.txt.
    Open a secondary window to display the game information.

    Returns
    -------
    None.

    """
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.resizable(0,0)
    aboutWindow.mainloop()