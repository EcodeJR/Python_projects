import pywhatkit
try:
    pywhatkit.info("web design", lines = 5)
    print("success...")
except:
    print("Unexpected error...Check internet connnection")