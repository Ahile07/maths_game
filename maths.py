from tkinter import *
import random
import time

SCORE = 0

# intrebari
def questions(): 
    
    global SCORE

    for question in range(3):
        number1 = random.randint(1,9)
        number2 = random.randint(1,9)

        result = int(number1 + number2)
        print(f"Question {question + 1}")
        rez = input(f"How much is {number1} + {number2} = ?: ")
        rezultat = int(rez)

        if rezultat == result:
            SCORE += 1

    print(f"Your score is: {SCORE}")

questions()

# timer
def timer():
    total_seconds = 3

    # Run the countdown
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
