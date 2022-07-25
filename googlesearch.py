import pywhatkit

user_input = input("what would you like to search")
try:
    pywhatkit.search(user_input)
    print("searching....")
except:
    print("error...Check internet connection")