import pywhatkit


search = input("Search")
try:
    pywhatkit.info(search, lines = 5)
    print("success...")
except:
    print("Unexpected error...Check internet connnection")
