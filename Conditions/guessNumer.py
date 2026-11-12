secret_number = 7

guess_count = 0

while guess_count < 3:
    guess = int(input("Guess number: "))
    guess_count+=1

    if guess == secret_number:
        print("You won!!!!")
        break
else:
    print("Sorry you gussed all wrong.")