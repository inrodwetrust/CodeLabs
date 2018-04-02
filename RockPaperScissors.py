import random
def main():
    print("Let's play rock, paper, scissors?")
    #call the user's guess
    user = user_selection()
    #call the computer's user_guess
    computer = computer_selection()
    #call the results function
    results(computer, user)

#computer number function
def computer_selection():
    #get a random number in range of 1 to 3
    computer = random.randrange(1,4)
    #if/elif statement
    if computer == 1:
        print("Computer chooses Rock.")
    elif computer == 2:
        print("Computer chooses Paper.")
    elif computer == 3:
        print("Computer chooses Scissors.")
        #return computer's computer_number
    return computer

# user selection function
def user_selection():
    # get the user selection
    user = input("Choose 'Rock', 'Paper', or 'Scissors' by typing that word. ")
    if is_valid_selection(user):
        if user == 'rock':
            user = 1
        elif user == 'paper':
            user = 2
        elif user == 'scissors':
            user = 3
        return user
    else:
        print('That response is invalid!')
        user_selection()

def is_valid_selection(user):
    if user =='rock' or 'paper' or 'scissors':
        status = True
    else:
        status = False
    return status


def restart():
    answer = input("Would you like to play again?  Enter 'y' for yes or 'n' for no: ")
    #if/elif statement
    if answer == 'y':
        main()
    elif answer == 'n':
        print("Goodbye!")
    else:
        print:("Please enter only 'y' or 'n'!")
        restart()


def results(computer, user):
    difference = computer - user
    if difference == 0:
        print("TIE!")
        restart()
    elif difference % 3 == 1:
        print("Wah, wah: You Lost :(")
        restart()
    elif difference % 3 == 2:
        print("Wicky Wicky!  You won :)")
        restart()

main()
