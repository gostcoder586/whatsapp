import pywhatkit
from datetime import datetime
from time import sleep
import keyboard
import re
import random

# you can add as many as messages in the below message list
message_list = ["hello", "hi", "hay", "hello!", "are you tare!"]
num = random.randint(0, len(message_list))
message = message_list[num]


def bomb():
    todays_date = datetime.now()
    pywhatkit.sendwhatmsg(number, message, todays_date.hour, todays_date.minute + 1)
    keyboard.press_and_release('Ctrl+w')
    sleep(60)
    bomb()


print(" Note: Make sure you login whatsapp web  ")
print("The programme wont stop until you stopped")
number = input("Enter Mobile Number with out country code: ")


def isvalid(number):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(number)


if isvalid(number):

    if len(number) == 10:
        number = "+91" + number
        bomb()
    else:
        print("Invalid Number")
else:
    print("Invalid Number")
