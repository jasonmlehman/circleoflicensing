from msgraphapi import msgraphapi
import json
import time
import os
import urllib3
import sys
import csv
from contextlib import closing
import requests
import gc
from datetime import datetime, timezone
import codecs

# Office 365 Credentials
o365creds = 'path to json credential file'

# Connet to Microsoft GraphAPI
graphapi = msgraphapi(o365creds)

# This generates a URL to a CSV which will have all your Office pro plus activations
url = graphapi.getsubs()

# This will be a dump of all users that have the potential to use Office Pro plus (all E3 users)
allusers = csv.writer(open("allusers.csv", 'w'), delimiter=':')
allusers.writerow(['upn','activated'])

# This is where we will write users that are using office pro plus that is in shared user mode (VDI or Citrix users)
# This is just interesting info
sharedw = csv.writer(open("sharedusers.csv", 'w'), delimiter=':')
sharedw.writerow(['upn','activated'])

#  This is the list of users we can potentially move back to E1 (or F3, or whatever deskless SKU is in use)
backtoe1 = csv.writer(open("backtoe1.csv", 'w'), delimiter=':')
backtoe1.writerow(['upn'])

with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
    for row in reader:
        if len(row) > 0 and row[1] != "(Unknown)" and '.onmicrosoft.com' not in row[1] and row[1] != "User Principal Name":
            reportdate = row[0]
            upn = row[1]
            dispname = row[2]
            product = row[3]
            activated = row[4]
            win = row[5]
            mac = row[6]
            win10mobile = row[7]
            ios = row[8]
            android = row[9]
            shared = row[10]
            # This gets the users that have no office activation.  If there are no activations I'm assuming a deskless user
            if activated == "":
                backtoe1.writerow([upn])
            if shared.lower() == "true" and win == "0" and mac == "0" and win10mobile == "0" and ios == "0" and android == "0":
                sharedw.writerow([upn,activated])
            allusers.writerow([upn,activated])
