import pywhatkit
from datetime import datetime
from time import sleep
import keyboard
import re


def bomb():
    todays_date = datetime.now()
    pywhatkit.sendwhatmsg(number, message, todays_date.hour, todays_date.minute + 1)
    keyboard.press_and_release('Ctrl+w')
    sleep(60)
    bomb()


print(" Note: Make sure you login whatsapp web  ")
number = input("Enter Mobile Number with out country code: ")


def isvalid(number):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(number)


if isvalid(number):

    if len(number) == 10:
        print("Valid Number Adding country code to the given number")
        number = "+91" + number
        message = input("Enter the Message : ")
        bomb()
    else:
        print("Invalid Number")
else:
    print("Invalid Number")
