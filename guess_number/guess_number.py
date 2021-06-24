import random

number = random.randint(0, 10000)
tries = 0
found = False

while not found:
    guess = int(input("guess:"))
    tries += 1
    if guess == number:
        found = True
        print(f"You Found The number {number} After {tries} Tries!")
    elif  guess > number:
        print(f"The Number You Are Looking For Is Less Than {guess}!")
    else:
        print(f"The Number You Are Looking For Is greater Than {guess}!")
