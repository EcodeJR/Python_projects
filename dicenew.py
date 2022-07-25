# Write your code here :-)
import random

dice = [1,2,3,4,5,6]

dicerand = random.choice(dice)

user = input("Enter R to roll the dice :\n").upper()
userroll = dicerand
print(userroll)
if userroll >= 4:
    print("Congrats you win")

else:
    print("you lost..try again")
