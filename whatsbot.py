import pywhatkit

try:
    message = pywhatkit.sendwhatmsg('+2348096548178', 'Checking the whats app bot trial 2', 12,5)
    print("Message sent!")
    
except:
    print("Unexpected Error!!!")
