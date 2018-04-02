import random

eyes = [':', ';', '8']
noses = ['o', '<', '>', 'O']
mouths = [')' , '(' , 'P']

# emoticon = (random.choice(eyes) + random.choice(noses) + random.choice (mouths))

i = 1
while i < 6:
    print(random.choice(eyes) + random.choice(noses) + random.choice (mouths))
    i = i + 1
