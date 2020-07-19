import random
import tkinter as tk
global wins, win, output, result
win = 0
result = ''
#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):
    global wins, win, output, result
    # Access variables declared after the function so that the variables can be changed inside of the function

    print(call)
    # 1. Create random integer 1-3 to use as computer's play
    rand_int = random.randint(1,3)

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if rand_int == 1:
        comp_choice = "rock"
    if rand_int == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"

    # 3. Determine the winner based on what the user chose and what the computer chose
    if call == "scissors":
        if comp_choice == "paper":
            win = win + 1
            result = "Result: You won!"
        else:
            pass
            result = "Result: You lost :("
    if call == "paper":
        if comp_choice == "rock":
            win = win + 1
            result = "Result: You won!"
        else:
            pass
            result = "Result: You lost :("
    if call == "rock":
        if comp_choice == "paper":
            win = win + 1
            result = "Result: You won!"
        else:
            pass
            result = "Result: You lost :("
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object
    # If the user wins, increase win by 1
    wins = "Number of wins: " + str(win)
    win_var.set(wins)
    print(win_var.get())
    result_var.set(result)
    print(result_var.get())


    # Use the output label to write what the computer did and what the result was (win, loss, tie)


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")


window = tk.Tk()

#Variable to count the number of wins the user gets

#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
paper = tk.Button(text = "paper", command = pass_p) #lambda: get_winner('paper'))

scissors = tk.Button(text = "scissors", command = pass_s) #lambda: pass_s())

rock = tk.Button(text = "rock", command = pass_r) #lambda: pass_r())

paper["command"] = pass_p
scissors["command"] = pass_s
rock["command"] = pass_r

# 2. Create 2 labels for the result and the number of wins
result_var = tk.StringVar()
win_var = tk.StringVar()


result_frame = tk.Frame(master = window)
result_label = tk.Label(master = result_frame, textvariable = result_var)
result_label.pack()

win_frame = tk.Frame(master = window)
win_label = tk.Label(master = win_frame, textvariable = win_var)
win_label.pack()

# 3. Arrange the buttons and labels using grid

result_frame.grid(row = 0, column = 1, padx= 5, pady = 5)
rock.grid(row = 1, column = 0, padx = 5, pady = 5)
paper.grid(row = 1, column = 1, padx = 5, pady = 5)
scissors.grid(row = 1, column = 2, padx = 5, pady = 5)
win_frame.grid(row = 2, column = 1, padx = 5, pady = 5)

window.mainloop()
