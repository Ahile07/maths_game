import random
import time

score = 0 

# scoruri
def flo(answer): 
    global score
    i = 3
    while i > 0:
        number1 = random.randint(1,9)
        number2 = random.randint(1,9)

        result = int(number1 + number2)

        rez = input(f"How much is {number1} + {number2} = ?: ")
        rezultat = int(rez)

        if answer == result:
            score += 1
        
        i -= 1

print(f"Your score is: {score}")

# timer
def timer():
    total_seconds = 3

    # Run the countdown
    while total_seconds > 0:
        print(total_seconds)
        total_seconds -= 1
        time.sleep(1)

    print("Time's up!")


flo(answer)
timer()
