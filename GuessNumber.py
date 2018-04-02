# computer randomly select an int from 1 to 10
# user then guesses a number
# program tell them if they are right or wrong
# user gets 5 chances to guess

import random

# randint includes the last number while randrange does not
compnum = random.randint(1, 10)

n = 1
while n < 6:
    usernum = int(input("Pick the correct number between 1 and 10: "))
    if compnum == usernum:
        print("You are correct and you are a winner with a chicken dinner!")
        exit(0)
    else:
        print("You did not guess correctly. ")
        n += 1
        if n == 6:
            print("The correct number was: ", compnum)
            exit(0)
