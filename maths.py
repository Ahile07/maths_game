from tkinter import *
import random
import time

# intrebari
def questions_player(player_name, nr_games): 
    
    score = 0

    for question in range(nr_games):
        number1 = random.randint(1,9)
        number2 = random.randint(1,9)

        operator_matematic = ["+","-","*"]
        mathematical_operation = random.choice(operator_matematic)
        
        if mathematical_operation == "+":
            result = int(number1 + number2)
        elif mathematical_operation == "-":
            result = int(number1 - number2)
        else:
            result = int(number1 * number2)

        print(f"{player_name}'s question number {question + 1}")
        rez = input(f"How much is {number1} {mathematical_operation} {number2} = ?: ")
        rezultat = int(rez)

        if rezultat == result:
            score += 1
        
    return score

# Find who is the winner
def winner(SCORE_PLAYER1, SCORE_PLAYER2, player1_name, player2_name):
    if SCORE_PLAYER1 == SCORE_PLAYER2:
        print("TIE! Well done both!!")
    elif SCORE_PLAYER1 > SCORE_PLAYER2:
        print(f"Congrats {player1_name}, you have WON with a score of \n{player1_name} - {SCORE_PLAYER1} vs {SCORE_PLAYER2} - {player2_name}")
    else:
        print(f"Congrats {player2_name}, you have WON with a score of \n{player1_name} - {SCORE_PLAYER1} vs {SCORE_PLAYER2} - {player2_name}")

# timer
def timer():
    total_seconds = 3

# Run the countdown - (Neimplementat inca)
    while total_seconds > 0:
        print(total_seconds)
        total_seconds -= 1
        time.sleep(1)

    print("Time's up!")

# GUI Game (Neimplementat inca)
def submit_players_names():
    Label(master,text= "Player 1 name: ", font=("Bebas Neue",20)).grid(row=3,sticky=W)
    player1_name = Entry(master).grid(row=3,sticky=W, padx=110)

    Label(master,text= "Player 2 name: ", font=("Bebas Neue",20)).grid(row=4,sticky=W)
    player2_name = Entry(master).grid(row=4,sticky=W, padx=110)

    #Main Screen
    master = Tk()
    master.title("BrainMaths")

    #Labels
    Label(master,text="How good are you with maths?",font=("Bebas Neue",30)).grid(row=0,sticky=W,pady=10,padx=50)
    #Space row 1
    Label(master,text= " ", font=("Bebas Neue",20)).grid(row=1,sticky=W)

    #Space row 5
    Label(master,text= " ", font=("Bebas Neue",20)).grid(row=5,sticky=W)

    submit_players_names()

    #Button players
    submit_names = Button(master, text = "Sumbit names", command=submit_players_names)


#-------------------------------
#inceputul jocului
def joc():

    SCORE_PLAYER1 = 0
    SCORE_PLAYER2 = 0

    player1_name = input("Please input player 1 name and hit enter: \n")
    player2_name = input("Please input player 2 name and hit enter: \n")

    how_many_games = int(input("How many games you want to play (1-10)? \n"))

    print(f"Hey {player1_name}! \nNGet ready!")
    time.sleep(3)

    if type(how_many_games) != int:
        print("Please use a number")

    SCORE_PLAYER1 += questions_player(player1_name, how_many_games)
    print(f"Thank you {player1_name}! \nNow is {player2_name}'s turn! \nGet ready!")
    time.sleep(3)
    SCORE_PLAYER2 += questions_player(player2_name, how_many_games)
    
    winner(SCORE_PLAYER1, SCORE_PLAYER2, player1_name, player2_name)

joc()