from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = Tk()
window.title("TIC-TAC-TOE")
window.resizable(0,0)
window.geometry("450x640")

clicked = True
count = 0

def btn_click(btn):
    global clicked, count
    if btn["text"] == " " and clicked == True:
        btn["text"] = "X"
        btn["bg"] = "powderblue"
        clicked = False
        count += 1
        win()

    elif btn["text"] == " " and clicked == False:
        btn["text"] = "O"
        btn["bg"] = "green"
        clicked = True
        count += 1
        win()

    else:
        messagebox.showerror("TIC-TAC-TOE", "Button already clicked")

def reset():
    global clicked, count
    li = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in li:
        i["bg"] = "white"
        clicked = True
        count = 0
        i["text"] = " "

# reset button

reset_btn = Button(window, text="RESET", width=20, height=8, command=reset)
reset_btn.place(x=150,y=510)

# Player Names Entries

def Player_Names():
    global player1, player2
    player1 = Entry(window, width=20, font=("Arial Bold", 20), fg="powderblue")
    player2 = Entry(window, width=20, font=("Arial Bold", 20), fg="green")
    player1.place(x=100 ,y=0)
    player2.place(x=100, y=50)
    player1.focus()

# Check if someone wins

def win():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        if player1.get() != "":
            messagebox.showinfo("TIC-TAC-TOE", "{} Wins".format(player1.get()))
            reset()
            winner = True

        else:
            messagebox.showinfo("TIC-TAC-TOE", "X Wins")
            reset()
            winner = True

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        if player1.get() != "":
            messagebox.showinfo("TIC-TAC-TOE", "{} Wins".format(player1.get()))
            reset()
            winner = True

        else:
            messagebox.showinfo("TIC-TAC-TOE", "X Wins")
            reset()
            winner = True

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        if player1.get() != "":
            messagebox.showinfo("TIC-TAC-TOE", "{} Wins".format(player1.get()))
            reset()
            winner = True

        else:
            messagebox.showinfo("TIC-TAC-TOE", "X Wins")
            reset()
            winner = True


    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        if player1.get() != "":
            messagebox.showinfo("TIC-TAC-TOE", "{} Wins".format(player2.get()))
            reset()
            winner = True

        else:
            messagebox.showinfo("TIC-TAC-TOE", "O Wins")
            reset()
            winner = True

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        if player1.get() != "":
            messagebox.showinfo("TIC-TAC-TOE", "{} Wins".format(player2.get()))
            reset()
            winner = True

        else:
            messagebox.showinfo("TIC-TAC-TOE", "O Wins")
            reset()
            winner = True

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        if player1.get() != "":
            messagebox.showinfo("TIC-TAC-TOE", "{} Wins".format(player2.get()))
            reset()
            winner = True

        else:
            messagebox.showinfo("TIC-TAC-TOE", "O Wins")
            reset()
            winner = True

    elif count == 9 and winner == False:
        messagebox.showinfo("TIC-TAC-TOE", "This is a TIE")
        reset()

# Player 1 Labels

player1_lbl = Label(window, text="Player 1", font=("Arial Bold", 15), fg="powderblue")
player2_lbl = Label(window, text="Player 2", font=("Arial Bold", 15), fg="green")
player1_lbl.place(x=0,y=0)
player2_lbl.place(x=0,y=50)
    

# Buttons

def Buttons():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    b1 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b1))
    b2 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b2))
    b3 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b3))
    b4 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b4))
    b5 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b5))
    b6 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b6))
    b7 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b7))
    b8 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b8))
    b9 = Button(window, text=" ", width=20, height=8, command = lambda : btn_click(b9))

# Displaying Buttons

def Display_Buttons():
    b1.place(x=0,y=150)
    b2.place(x=150,y=150)
    b3.place(x=300,y=150)
    b4.place(x=0,y=280)
    b5.place(x=150,y=280)
    b6.place(x=300, y=280)
    b7.place(x=0,y=410)
    b8.place(x=150,y=410)
    b9.place(x=300,y=410)


# Calling Functions

Buttons()
Display_Buttons()
Player_Names()

# Calling The Main Loop (running the TIC-TAC-TOE Game)

window.mainloop()