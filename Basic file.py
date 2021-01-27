import pywhatkit
import re

print(" Note: Make sure you login whatsapp web  ")
number = input("Enter Mobile Number with out country code: ")


def isvalid(number):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(number)


if (isvalid(number)):

    if len(number) == 10:
        print("Valid Number Adding country code to the given number")
        number = "+91" + number
        message = input("Enter the Message : ")
        time = input("Enter Time without spaces (HHMMSS)")
        time_hour = int(time[0:2])
        time_min = int(time[2:4])
        time_sec = int(time[4:6])
        print("Your Message {} will be send to {} at {}".format(message, number, time))
        pywhatkit.sendwhatmsg(number, message, time_hour, time_min, time_sec)
    else:
        print("Invalid Number")
else:
    print("Invalid Number")
