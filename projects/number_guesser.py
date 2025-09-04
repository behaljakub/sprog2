import random

number = random.randint(1, 100)

print(number)


attempts = 3
while attempts > 0:
    guess_number = int(input("Guess your number: "))
    attempts -= 1
    if guess_number > number:
        print("Too high")
    elif guess_number < number:
        print("Too low")
    elif guess_number == number:
        print("You win")
        break


else:
    print("You lost")
    



