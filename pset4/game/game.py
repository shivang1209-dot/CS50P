import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        continue

x = random.randint(1,n)
guess = 0
while guess != x:
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == x:
                print("Just right!")
                break
            elif guess < x:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            pass

