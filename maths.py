from tkinter import *
import random
import time

def questions_player(player_name, nr_games): 
    """
    Ask random questions and calculates the score:
    
    Inputs:
    player_name: string, name of player that is asked
    nr_games: int, number of questions to be asked
    
    Outputs:
    score: int, number of questions with correct answer

    """
    
    # score should always start from 0
    score = 0

    # ask the number of questions
    for question in range(nr_games):
        
        #assign random values to questions
        number1 = random.randint(1,9)
        number2 = random.randint(1,9)

        #chose a random operator from a list
        operator_matematic = ["+","-","*"]
        mathematical_operation = random.choice(operator_matematic)
        
        if mathematical_operation == "+":
            result = int(number1 + number2)
        elif mathematical_operation == "-":
            result = int(number1 - number2)
        else:
            result = int(number1 * number2)

        #ask the question
        print(f"\n{player_name}'s question number {question + 1}")

        #wait for result
        rez = input(f"\nHow much is {number1} {mathematical_operation} {number2} = ?: ")
        rezultat = int(rez)

        #check correction
        if rezultat == result:
            score += 1
        
    return score

def winner(SCORE_PLAYER1, SCORE_PLAYER2, player1_name, player2_name):
    """
    Compares scores of the 2 players and it prints who the winner is.

    """
    # compares the scores of the 2 players
    if SCORE_PLAYER1 == SCORE_PLAYER2:
        print(f"\nTIE! Well done both!!\n")
    elif SCORE_PLAYER1 > SCORE_PLAYER2:
        print(f"\nCongrats {player1_name}, you have WON with a score of \n{player1_name} - {SCORE_PLAYER1} vs {SCORE_PLAYER2} - {player2_name}\n")
    else:
        print(f"\nCongrats {player2_name}, you have WON with a score of \n{player1_name} - {SCORE_PLAYER1} vs {SCORE_PLAYER2} - {player2_name}\n")


def timer():
    """
    Counts down the number of seconds:

    Inputs:
    total_seconds: int, number of seconds to count down

    """

    total_seconds = 3

    # Run the countdown - (Neimplementat inca)
    while total_seconds > 0:
        print(total_seconds)
        total_seconds -= 1
        time.sleep(1)

    print("Time's up!")


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


#inceputul jocului
def joc():

    SCORE_PLAYER1 = 0
    SCORE_PLAYER2 = 0

    player1_name = input("Please input player 1 name and hit enter: \n")
    player2_name = input("\nPlease input player 2 name and hit enter: \n")

    how_many_games = int(input("\nHow many games you want to play (1-10)? \n"))

    print(f"\nHey {player1_name}! \nGet ready!\n")
    time.sleep(3)

    if type(how_many_games) != int:
        print("Please use a number")

    SCORE_PLAYER1 += questions_player(player1_name, how_many_games)
    print(f"\nThank you {player1_name}! \nNow is {player2_name}'s turn! \nGet ready!\n")
    time.sleep(3)
    SCORE_PLAYER2 += questions_player(player2_name, how_many_games)
    
    winner(SCORE_PLAYER1, SCORE_PLAYER2, player1_name, player2_name)

joc()