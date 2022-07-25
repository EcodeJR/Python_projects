#3list["a","b","c"]
#1 first letter of the site/platform name turn it to capital letter
#4month of birth select the second and last numbers
#2random number from range 1,100
import random
print("Password Generator")

num_list = ["a","b","c","d"]
first_alphabeth = num_list[2]
second_alphabeth = num_list[-1]
#print(num_list)
#rand_num = [1,2,3,4,5,6,7,8,9,0]
user_site = str(input("Name of site/account you would like to open :\n")).upper()
user_site_letter = user_site[0]
user_month = str(input("Enter your month of birth :\n"))
#birth_month = user_month
numb = random.randrange(1,100)
#letters = random.sample(num_list, 2)
#password = user_site_letter + numb + letters + birth_month
print(f"Your suggested password is: {user_site_letter}{numb}{first_alphabeth}{user_month}")

#rand_password = ''.join(random.sample({user_site_letter,numb,letters,birth_month}))
'''
print(user_site_letter)
print(numb)
print(letters)
print(user_month)
print(rand_password)
'''