import random
passwords = str(["ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst1234567890!@#$%^&*()_+/.,;"])
print("WELCOME USER")
print("Follow all instructions to generate your uniqe password")

user_name = input("Enter your Name  :\n")
user_account = input("Which account are your generating password for? :\n")
#name.append(user_name)
#account.append(user_account)

rand_password = ''.join(random.sample(passwords, 20))

print(user_name, "Your password for", user_account, "is")
print(rand_password)
print("Remember not to share it with anyone :\n Be safe")