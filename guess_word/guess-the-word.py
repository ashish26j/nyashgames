word = "secret"

Allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors Left {Allowed_errors}, Next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        Allowed_errors -= 1
        if Allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You Found The Word! it was {word}")
else:
    print(f"Gmae Over! The Word was {word}!")