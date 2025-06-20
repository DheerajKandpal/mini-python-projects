import random
attempts = 5
secret_number = random.randint(1, 50)
gussing_number = int(input("Input a guess between 1 and 50:"))
while attempts > 0:
    if gussing_number == secret_number:
        print ("congratulations! You guessed the number!")
        break
    elif gussing_number <secret_number:
        print("too low!")
    else :
        print("too high")

    attempts -= 1
    gussing_number = int(input("Input a guess between 1 and 50: "))
else:
        print(f"Game over! The number was {secret_number}.")
