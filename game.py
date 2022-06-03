from random import Random


number = Random(1,2,3,4,5,6,7,8,9)
chances = 0
guess = input("Guess a number between 0 to 9")
while chances < 5:
    chances = chances+1
    a = number
    if guess == number:
        print("Congrats! You guessed the right number")
    else:
        print("Try Again")
    break
if not chances < 5:
    print("You are out of chances. The correct number was ", number)