import random
import threading
from datetime import datetime
from time import *

import pywhatkit

msg = random.randint(0, 4)
messagelist = ['Hi', 'Hello', 'hay', 'hlo', 'are you tare!']
message = messagelist[msg]
number1 = ["+91 9553525912", "+91 6302 584 117", "+91 99637 07389"]


def sender1():
    for i in number1:
        todays_date = datetime.now()
        print("sender1" + i, todays_date.hour, todays_date.minute + 1)
        sleep(60)
        pywhatkit.sendwhatmsg(i, message, todays_date.hour, todays_date.minute + 1)


t1 = threading.Thread(target=sender1)
t1.start()
t1.join()
print('All Messages Send successfully')
