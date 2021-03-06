# main.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import urequests, machine, time
from config import *

# MailNinja Notification
hook = urequests.get((webhook))

# show network status
status = urequests.get('https://raw.githubusercontent.com/nwgat/mailboxninja/master/status')
print ('--------------------')
print ('Internet Status:', (status.text))
print ('--------------------')

# Power Saving mode (RST + GND to wake up with a reed door sensor)
time.sleep(30)
machine.deepsleep()
