import random as rnd
import tkinter as tk

plvalue = ""
values = ["rock", "paper", "scissors"]
cmp_value = ""
plscore = 0
cmpscore = 0
drawed_times = 0

def game(player, cmp):
    global plscore
    global cmpscore
    global drawed_times

    if player == cmp:
        lblconfig(lbl_winner, "draw!")
        drawed_times = drawed_times + 1
        lblconfig(draw_lbl, str(drawed_times))
        return
    
    if player == "rock":
        if cmp == "paper":
            lblconfig(lbl_winner, "computer wins")
            cmpscore = cmpscore + 1
            lblconfig(cmp_score_lbl, str(cmpscore))
            return
        
        if cmp == "scissors":
            lblconfig(lbl_winner, "player wins")
            plscore = plscore + 1
            lblconfig(player_score_lbl, str(plscore))
            return
        
    if player == "paper":
        if cmp == "scissors":
            lblconfig(lbl_winner, "computer wins")
            cmpscore = cmpscore + 1
            lblconfig(cmp_score_lbl, str(cmpscore))
            return
        
        if cmp == "rock":
            lblconfig(lbl_winner, "player wins")
            plscore = plscore + 1
            lblconfig(player_score_lbl, str(plscore))
            return
    
    if player == "scissors":
        if cmp == "rock":
            lblconfig(lbl_winner, "computer wins")
            cmpscore = cmpscore + 1
            lblconfig(cmp_score_lbl, str(cmpscore))
            return
        
        if cmp == "paper":
            lblconfig(lbl_winner, "player wins")
            plscore = plscore + 1
            lblconfig(player_score_lbl, str(plscore))
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

win.resizable(False, False)

main_icon = tk.PhotoImage(file='main logo.gif')
win.iconphoto(True, main_icon)
win.title('R,P,S')

lbl_player = tk.Label(win, text="avalable choices:")
lbl_player.pack()

######################## create btn_frame and player buttons ######################
rock_icon = tk.PhotoImage(file='rock.png')
paper_icon = tk.PhotoImage(file='paper.png')
scissors_icon = tk.PhotoImage(file='scissors.png')

btn_frame = tk.Frame(win)
btn_frame.columnconfigure(0, weight=1)

plrock = tk.Button(btn_frame,image=rock_icon, padx=10, pady=10, command=plrock)
plpaper = tk.Button(btn_frame, image=paper_icon, padx=10, pady=10, command=plpaper)
plscissors = tk.Button(btn_frame, image=scissors_icon, padx=10, pady=10, command=plscissors)
plrandom = tk.Button(btn_frame, text="random choice",image=main_icon, padx=10, pady=10, compound="bottom", command=plrandom)

plrock.grid(row=0, column=0)
plpaper.grid(row=0, column=1)
plscissors.grid(row=0, column=2)
plrandom.grid(row=0, column=3)

btn_frame.pack()
###############################################################################
lbl_players_choice = tk.Label(win, text="__")
lbl_players_choice.pack()

lbl_cmp = tk.Label(win, text="compouter's choice:")
lbl_cmp.pack()

cmp_choice = tk.Label(win, text="__")
cmp_choice.pack()

lbl_winner = tk.Label(win, text="__")
lbl_winner.pack()
######======making player and computers score holder btn_frame =======#######
score_frame = tk.Frame(win)

player_score_msg_lbl = tk.Label(score_frame, text="player's score:")
player_score_lbl = tk.Label(score_frame, text=str(plscore))
cmp_score_msg_lbl = tk.Label(score_frame, text="computer's score:")
cmp_score_lbl = tk.Label(score_frame, text=str(cmpscore))
draw_msg_lbl = tk.Label(score_frame, text="drawed rounds:")
draw_lbl = tk.Label(score_frame, text=str(drawed_times))

player_score_msg_lbl.grid(column=0, row=0)
player_score_lbl.grid(column=1, row=0)
cmp_score_msg_lbl.grid(column=0, row=1)
cmp_score_lbl.grid(column=1, row=1)
draw_msg_lbl.grid(column=0, row=2)
draw_lbl.grid(column=1, row=2)

score_frame.pack(pady=20)

win.mainloop()
###############################################################################
