import random

print("Random")
print("Welcome to random")
print("Instruction: You are to guess a number if it corresponds with ours you win")
my_random_no = random.randrange(1,10)
user_input = int(input("Enter a number from the range of 1 to 10 : \n"))
if user_input == my_random_no:print("Congratulations!!!!!!!")
    
else: print("oops wrong choice")
print(my_random_no)