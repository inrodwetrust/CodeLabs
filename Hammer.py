time = input("Enter the time of the day in military time with a colon: ")
split_time = time.split(":")
integer = int(split_time[0])

if integer in range(7,10):
    print("It's breakfast, bitch!")

elif integer in range(12,15):
    print("It's fucking lunch, stripper!")

elif integer in range(19,22):
    print("Din Din, ho-knuckles!")

elif integer in range(22,25):
    print("Hammertime")

elif integer in range(0,5):
    print("Hammertime")

else:
    print("It's DJ Franky Knuckles time.")
