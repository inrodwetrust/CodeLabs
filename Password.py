import string
import random

# Greeting
generator = 0
while generator < 5:
    print("Let's generate a good password for you.")

# this defines font size and character selection of specified strings
    def password(size = 12, chars = string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))

# prints the randomly generated password according to how many integers specified
    print(password(int(input("Enter the number of characters your password should be: "))))
    generator = generator + 1
