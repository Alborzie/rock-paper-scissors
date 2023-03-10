import random as rnd
import tkinter as tk

plvalue = ""
values = ["rock", "paper", "scissors"]
cmp_value = ""

def game(player, cmp):
    if player == cmp:
        lblconfig(lbl_winner, "draw!")
        return
    
    if player == "rock":
        if cmp == "paper":
            lblconfig(lbl_winner, "computer wins")
            return
        
        if cmp == "scissors":
            lblconfig(lbl_winner, "player wins")
            return
        
    if player == "paper":
        if cmp == "scissors":
            lblconfig(lbl_winner, "computer wins")
            return
        
        if cmp == "rock":
            lblconfig(lbl_winner, "player wins")
            return
    
    if player == "scissors":
        if cmp == "rock":
            lblconfig(lbl_winner, "computer wins")
            return
        
        if cmp == "paper":
            lblconfig(lbl_winner, "player wins")
            return
    
    
def lblconfig(lblname, txt):
    lblname.configure(text=txt)

def cmpvalue():
    global cmp_value
    cmp_value = rnd.choice(values)
    lblconfig(cmp_choice, cmp_value)
    
def plrock():
    global plvalue
    plvalue = "rock"
    lblconfig(lbl_players_choice, plvalue)
    cmpvalue()
    game(plvalue, cmp_value)
    
def plpaper():
    global plvalue
    plvalue = "paper"
    lblconfig(lbl_players_choice, plvalue)
    cmpvalue()
    game(plvalue, cmp_value)
    
def plscissors():
    global plvalue
    plvalue = "scissors"
    lblconfig(lbl_players_choice, plvalue)
    cmpvalue()
    game(plvalue, cmp_value)
    
def plrandom():
    global plvalue
    plvalue = rnd.choice(values)
    lblconfig(lbl_players_choice, plvalue)
    cmpvalue()
    game(plvalue, cmp_value)
    
################################### creating window ###########################
win = tk.Tk()

lbl_player = tk.Label(win, text="avalable choices:")
lbl_player.pack()

######################## create frame and player buttons ######################
frame = tk.Frame(win)
frame.columnconfigure(0, weight=1)

plrock = tk.Button(frame, text="rock", padx=10, pady=10, command=plrock)
plpaper = tk.Button(frame, text="paper", padx=10, pady=10, command=plpaper)
plscissors = tk.Button(frame, text="scissors", padx=10, pady=10, command=plscissors)
plrandom = tk.Button(frame, text="random", padx=10, pady=10, command=plrandom)

plrock.grid(row=0, column=0)
plpaper.grid(row=0, column=1)
plscissors.grid(row=0, column=2)
plrandom.grid(row=0, column=3)

frame.pack()
###############################################################################
lbl_players_choice = tk.Label(win, text="__")
lbl_players_choice.pack()

lbl_cmp = tk.Label(win, text="compouter's choice:")
lbl_cmp.pack()

cmp_choice = tk.Label(win, text="__")
cmp_choice.pack()

lbl_winner = tk.Label(win, text="__")
lbl_winner.pack()

win.mainloop()
###############################################################################
