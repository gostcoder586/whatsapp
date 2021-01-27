import pywhatkit
import threading
from datetime import datetime
from time import sleep
import keyboard
message = 'Wishing you & your loved ones a very Happy Pongal'

# added as many as mobile numbers you want in the  "" and add , at end
number = ["+91 111111111", "+91 2222222222 ", "+91 333333333333", "+91 44444444444"]


def sender():
    for i in number:
        todays_date = datetime.now()
        t = todays_date.hour, todays_date.minute + 1
        print("Your Message will be send to {} in {}  ".format(i, t))
        pywhatkit.sendwhatmsg(i, message, todays_date.hour, todays_date.minute + 1)
        keyboard.press_and_release('Ctrl+w')
        sleep(60)


t1 = threading.Thread(target=sender)
t1.start()
t1.join()

print('All Messages Send Successfully')
