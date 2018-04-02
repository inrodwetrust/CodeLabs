import random


# enter six choices
def user_matches():
    user_numbers = []
    n1 = int(input("Pick a number from 1 to 10: "))
    user_numbers.append(n1)
    n2 = int(input("Pick a number from 11 to 20: "))
    user_numbers.append(n2)
    n3 = int(input("Pick a number from 21 to 30: "))
    user_numbers.append(n3)
    n4 = int(input("Pick a number from 31 to 40: "))
    user_numbers.append(n4)
    n5 = int(input("Pick a number from 41 to 50: "))
    user_numbers.append(n5)
    n6 = int(input("Pick a number from 51 to 60: "))
    user_numbers.append(n6)
    return user_numbers


def winning_lotto_numbers():
    win_numbers = []
    win_numbers1 = random.randint(1, 10)
    win_numbers.append(win_numbers1)
    win_numbers2 = random.randint(11, 20)
    win_numbers.append(win_numbers2)
    win_numbers3 = random.randint(21, 30)
    win_numbers.append(win_numbers3)
    win_numbers4 = random.randint(31, 40)
    win_numbers.append(win_numbers4)
    win_numbers5 = random.randint(41, 50)
    win_numbers.append(win_numbers5)
    win_numbers6 = random.randint(51, 60)
    win_numbers.append(win_numbers6)
    return win_numbers


def compare_numbers(user, CPU):
    match = 0
    for index in range(len(user)):
        if user[index] == CPU[index]:
            match += 1
    return match


def payout(matches):
    winning_balance = 0
    if matches == 0:
        return winning_balance
    elif matches == 1:
        print("You won $4. Buy 2 tickets, this time.")
        winning_balance += 4
        return winning_balance
    elif matches == 2:
        print("You won $7...Whoopty doo.")
        winning_balance += 7
        return winning_balance
    elif matches == 3:
        print("You won $100! Make it rain!")
        winning_balance += 100
        return winning_balance
    elif matches == 4:
        print("You have won $50,000! Buy a new car!")
        winning_balance += 50000
        return winning_balance
    elif matches == 5:
        print("You just won $1,000,000! Buy a house!")
        winning_balance += 1000000
        return winning_balance
    elif matches == 6:
        print("You just won $25,000,000! Marry me!")
        winning_balance += 25000000
        return winning_balance

user_defined_numbers = user_matches()
print(user_defined_numbers)
plays = int(input("How many times will you play these numbers?: "))
balance = 0
while plays > 0:
    balance -= 2
    CPU_numbers = winning_lotto_numbers()
    print("Your picks are: ", user_defined_numbers)
    print("Powerball Numbers: ", CPU_numbers)

    final_matches = compare_numbers(user_defined_numbers, CPU_numbers)
    print("Matches: ", final_matches)

    winning_amount = payout(final_matches)
    print("the winnings are: ", winning_amount)
    balance += winning_amount
    print("Balance Overall: %s" % balance)
    plays -= 1





