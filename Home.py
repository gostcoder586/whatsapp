# import random
# import threading
# import keyboard
# import pywhatkit
# from datetime import datetime
# from time import *
#
# msg = random.randint(0, 4)
# messagelist = ['Hi', 'Hello', 'hay', 'hlo', 'are you tare!']
# message = messagelist[msg]
# number = ["+91 9553525912", "+91 6302 584 117", "+91 99637 07389"]
#
#
# def sender1():
#     for i in number:
#         todays_date = datetime.now()
#         print(i, todays_date.hour, todays_date.minute + 1)
#         pywhatkit.sendwhatmsg(i, message, todays_date.hour, todays_date.minute + 1)
#         sleep(60)
#         keyboard.press_and_release('ctrl+w')
#
#
# t1 = threading.Thread(target=sender1)
# t1.start()
# t1.join()
# print('All Messages Send successfully')
import csv
with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Phone 1 - Type'], row['Phone 1 - Value'])
