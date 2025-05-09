from tkinter import*
import random

def next_turn(row,column):
    
    global player

    if buttons[row][column]['text']== "" and check_winner() is False:

        if player== players[0]:

            buttons[row][column]['text']= player

            if check_winner() is False:
                player=players[1]
                label.config(text=(player[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(player[0]+" Wins"))

            elif check_winner() == "tie":
                label.config(text=("Tie!"))
        
        else:

            buttons[row][column]['text']= player

            if check_winner() is False:
                player=players[0]
                label.config(text=(player[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(player[0]+" Wins"))

            elif check_winner() == "tie":
                label.config(text=("Tie!"))

def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    
    for column in range(3):
        if buttons[column][0]['text'] == buttons[column][1]['text'] == buttons[column][2]['text'] != "":
            buttons[column][0].config(bg="green")
            buttons[column][1].config(bg="green")
            buttons[column][2].config(bg="green")
            return True
         

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True 

    elif buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][0].config(bg="green")
        buttons[2][0].config(bg="green")
        return True 
    
    elif buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text'] != "":
        buttons[0][1].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][1].config(bg="green")
        return True
        
    elif buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][2].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range (3):
            for column in range (3):
                buttons[row][column].config(bg="yellow")
        return 'Tie'

    else:
        return False      

def empty_spaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    
    global player

    player = random.choice(players)
    
    label.config(text=player+"true")

    for row in range (3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#f0f0f0")

window = Tk()
window.title("Tic-Tak-Toe")
players = ["X","O"]
player =random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text=player + " Turn", font=('consoles',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('console', 20), command = new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('console',48), width=5,height=2, command = lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()