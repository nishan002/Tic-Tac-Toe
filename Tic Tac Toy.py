from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ActivePlayer = 1
p1 = []
p2 = []

root = Tk()
root.title("Tic Tac Toy: Player 1")

button1 = ttk.Button(root, text=' ')
button1.grid(row=0, column=0, sticky='news', ipadx=40, ipady=40)
button1.rowconfigure(0, weight=1)
button1.config(command=lambda: Button_clicked(1))

button2 = ttk.Button(root, text=' ')
button2.grid(row=0, column=1, sticky='news', ipadx=40, ipady=40)
button2.rowconfigure(0, weight=1)
button2.config(command=lambda: Button_clicked(2))

button3 = ttk.Button(root, text=' ')
button3.grid(row=0, column=2, sticky='news', ipadx=40, ipady=40)
button3.rowconfigure(0, weight=1)
button3.config(command=lambda: Button_clicked(3))

button4 = ttk.Button(root, text=' ')
button4.grid(row=1, column=0, sticky='news', ipadx=40, ipady=40)
button4.config(command=lambda: Button_clicked(4))

button5 = ttk.Button(root, text=' ')
button5.grid(row=1, column=1, sticky='news', ipadx=40, ipady=40)
button5.config(command=lambda: Button_clicked(5))

button6 = ttk.Button(root, text=' ')
button6.grid(row=1, column=2, sticky='news', ipadx=40, ipady=40)
button6.config(command=lambda: Button_clicked(6))

button7 = ttk.Button(root, text=' ')
button7.grid(row=2, column=0, sticky='news', ipadx=40, ipady=40)
button7.config(command=lambda: Button_clicked(7))

button8 = ttk.Button(root, text=' ')
button8.grid(row=2, column=1, sticky='news', ipadx=40, ipady=40)
button8.config(command=lambda: Button_clicked(8))

button9 = ttk.Button(root, text=' ')
button9.grid(row=2, column=2, sticky='news', ipadx=40, ipady=40)
button9.config(command=lambda: Button_clicked(9))


def Button_clicked(id):
    global ActivePlayer
    global p1
    global p2

    if(ActivePlayer == 1):
        SetLayout(id, "X")
        p1.append(id)
        root.title("Tic Tac Toy : Player 2")
        ActivePlayer = 2
        print("P1 : {}".format(p1))

    elif(ActivePlayer == 2):
        SetLayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toy : Player 1")
        ActivePlayer = 1
        print("P2 : {}".format(p2))

    Check_Winner()

def SetLayout(id, PlayerSymbol):
    if id == 1:
        button1.config(text=PlayerSymbol)
        button1.state(['disabled'])
    elif (id == 2):
        button2.config(text=PlayerSymbol)
        button2.state(['disabled'])
    elif (id == 3):
        button3.config(text=PlayerSymbol)
        button3.state(['disabled'])
    elif (id == 4):
        button4.config(text=PlayerSymbol)
        button4.state(['disabled'])
    elif (id == 5):
        button5.config(text=PlayerSymbol)
        button5.state(['disabled'])
    elif (id == 6):
        button6.config(text=PlayerSymbol)
        button6.state(['disabled'])
    elif (id == 7):
        button7.config(text=PlayerSymbol)
        button7.state(['disabled'])
    elif (id == 8):
        button8.config(text=PlayerSymbol)
        button8.state(['disabled'])
    elif (id == 9):
        button9.config(text=PlayerSymbol)
        button9.state(['disabled'])

def Check_Winner():
    winner = -1
    # Player 1 winning situation
    if((1 in p1) and (2 in p1) and(3 in p1)):
        winner=1
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1

    # Player 2 winning situation
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner = 2
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner = 2
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner = 2
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner = 2
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner = 2
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner = 2
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner = 2
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2

    if winner==1:
        messagebox.showinfo(title="Congrats", message="Player 1 is the Winner")
    elif winner==2:
        messagebox.showinfo(title="Congrats", message="Player 2 is the Winner")

root.mainloop()
