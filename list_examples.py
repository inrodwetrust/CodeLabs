string = "I am a string!"
integer = 3

lst = [string, integer, 4, "the", [1,2,3.14]]
print(lst[4][1]) #will give us 2
print(lst[1:]) #this is from 1 to the end
print(lst[1:3]) #this will print 2 upto 3, but not 1 or 3

number = list(range(100))
print(number[len(number) - 1])

word = '7 AM'
split_word = word.split()
print(split_word[0]) # will return 7 
