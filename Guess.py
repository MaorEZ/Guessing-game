import random

num = random.randint(1, 10)

name = input("Hey, What's Your name?: ")

print("Hey " + name.capitalize() + " My name is Anaconda")
question = input("Would you like to play a game " + name.capitalize() + "? Y/N: ")

if question.lower() not in ("no", "n", "yes", "y", "nope", "yep", "idk"):
    print("Invalid answer BITCH, ANSWER YES OR NO")
    exit()

if question.lower() == "idk":
    print("What do you mean you don't know?, bye")
    exit()
if question.lower() in ("no", "n", "nope"):
    print("Oh, Maybe another time")
    exit()
else:
    print("Great let's start!, I'm thinking of a number between 1-10")


while True:
    try:

        guess = int(input("You have 3 tries Try guessing: "))
        while guess >= 11:
            print("Please only enter numbers between 1-10")
            guess = int(input("Still 1st guess Try again: "))
        else:
            if guess > num:
                print("Wrong answer try lower")
                break
            elif guess < num:
                print("Wrong answer try higher")
                break
            elif guess == num:
                print("You WON, 1st TRY AMAZING, the number was", num)
                exit()
    except ValueError:
        print('Enter a number Dumbass')
        continue

while True:
    try:

        guess = int(input("2nd Try GL!: "))
        while guess >= 11:
            print("Please only enter numbers between 1-10")
            guess = int(input("Still 2nd Try: "))
        else:
            if guess > num:
                print("Wrong again? Oof, go lower")
                break
            elif guess < num:
                print("Wrong again? Oof, go higher")
                break
            elif guess == num:
                print("You WON, 2nd try.. decent, the number was", num)
                exit()
    except ValueError:
        print('Stop messing around, Enter a number')
        continue

while True:
    try:

        guess = int(input("Last try YOU CAN DO IT!: "))
        while guess >= 11:
            print("Please only enter numbers between 1-10")
            guess = int(input("Still 3rd and last try: "))
        else:
            if guess != num:
                print("Damn, The number was", num, "That was the last try GL Next time")
                exit()
            elif guess == num:
                print("You WON, 3rd try... Ok I guess, The number was", num)
                exit()
    except ValueError:
        print('You seriously still TROLLING? ENTER A NUMBER, STOP MESSING AROUND')
        continue
