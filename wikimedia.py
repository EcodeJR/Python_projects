import pywhatkit

print("Wikimedia")
print("Welcoome to wikimedia\n Where you get information on any topic:\n")
user = input("Enter your Name:\n")
resone = input("What would you be doing with the information provided:\n")
user_search = input("What do you want to know:\n")

try:
    pywhatkit.search(user_search)
    print("Success")
    print(user, "Hope this what your looking for.")
except:
    print("Error check your internet connection...") 