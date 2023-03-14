# ******************************************************
# Python Tic Tac Toe game
# ******************************************************

#tkinter is a standard GUI library function for python
from tkinter import *
import random

#Function for next turn in game.
def next_turn(row, column):

    global turn

    if board[row][column]['text'] == "" and check_winner() is False:

        if turn == players[0]:

            board[row][column]['text'] = turn

            if check_winner() is False:
                turn = players[1]
                label.config(text=(players[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            board[row][column]['text'] = turn

            if check_winner() is False:
                turn = players[0]
                label.config(text=(players[0]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

#Function for checking winner.
def check_winner():

 #For vertical line.
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            board[row][0].config(bg="green")
            board[row][1].config(bg="green")
            board[row][2].config(bg="green")
            return True
 #For horizontal line.
    for column in range(3):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != "":
            board[0][column].config(bg="green")
            board[1][column].config(bg="green")
            board[2][column].config(bg="green")
            return True
 #For two diagonal lines
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        board[0][0].config(bg="green")
        board[1][1].config(bg="green")
        board[2][2].config(bg="green")
        return True

    elif board[0][2]['text'] == board[1][1]['text'] ==board[2][0]['text'] != "":
        board[0][2].config(bg="green")
        board[1][1].config(bg="green")
        board[2][0].config(bg="green")
        return True
 # For no empty space
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                board[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

#Function for checking empty space.
def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if board[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True
#Function for creating new game after click restart button
def new_game():

    global turn

    turn = random.choice(players)

    label.config(text=turn+" Turn")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",bg="lightgray")


window = Tk()
window.title("Tic-Tac-Toe")

#Define 2players.
players = ["x","o"]
#Select random turn
turn = random.choice(players)

#Create 2D list.
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
#Game title.
titlelabel=Label(text="Tic-Tac-Toe Game", font=("Copperplate Gothic Bold",20), bg="lightblue")
titlelabel.pack(side="top")

#Display which player turns.
label = Label(text=turn + " Turn", font=('consolas',25))
label.pack(side="top")

#Create restart button.
reset_button = Button(text="Restart", font=('consolas',20), bg="lightblue", command=new_game)
reset_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

#Define row & column size,bg colour,font etc.
for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="",font=('consolas',45), width=5, height=2, bg="lightgray",
                                      command= lambda row=row, column=column: next_turn(row,column))
        board[row][column].grid(row=row,column=column)

window.mainloop()


