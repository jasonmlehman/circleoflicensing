# Free'ing up Microsoft licenses!

Busineses that use Office 365 often have various levels of Microsoft licenses that may include standard and enhanced licenses.  For example, let's say you're in manufacturing and you have users that only need a Kiosk license or even an office only (F3/E1, etc) license.  These licenses are MUCH cheaper than the Microsoft enhanced licenses like E3/E5.  Often times businesses find themselves in a position where they have an astronomical bill when it's time to true up licenses.  

Why does this happen?  Most place don't have a solid licensing provision process and users find ways to get the enhanced licenses even though they don't need them. This job servers as a tacticle response to the ballooning of enhanced licenses.  To make this work long term you would need a special process designed specifically for your organization.  I call it "The circle of Licensing."  With automation we can see if the enhanced license has been consumed by a user that it is assigned to.  If it hasn't been used, then that user gets downgraded to the standard license.  You will need a solid request process for the user to re-request the enhanced license.

I could do this in powershell as well, I just choose not to.

# Installation

You will need my msgraphapi.  Follow the instructions to setup your connection below.

* pip install git+https://github.com/jasonmlehman/msgraphapi.git

# How?

Glad you asked.  How do I determine if a user is using a license or not?  Think about the SKU's and what is really determing if a user is using that SKU.  A simple comparison might be an F3 and an E3 user.  The only "real" difference might be with the deskless users and whether those users have activated office Pro Plus.  If they aren't using Office Pro Plus why do they have the license?  Mobile, Teams, Onedrive are no different between the SKU's.  So, if we can determine who has activiated Office pro plus within a specified time period then we can assume that user doesn't need enhanced licensing.

There might be other reasons (at times) that a user needs the enhanced license.  Litigation hold might be a reason to give a user the enhanced license but that is only temporary and you can put in operational processes to account for that.

This will not work for everyone.  This just gets a list of users that have no office pro plus activations.  If they don't have an activation ask yourself why they are getting an enhanced license?  Does the user need a large mailbox? Does the user need shared mailboxes?  If so, you can add other exchange online powershell scripts to query those users to see if they are using those functions.

You can check users  creation date in active directory and only move users back to E1/F3 if their account has been active for more than 30 days (gives users time to get a device and activate office). You might check device logins to see if the user may have a dedicated device (for F3).

Use this as a starting point.

# Not a python guru and need help getting this going?

1) Download python: https://www.python.org/downloads/release/python-382/

2) Run this command to install the graphAPI libraries

   pip install git+https://github.com/jasonmlehman/msgraphapi.git

3) Download checklicensing.py from this repo: https://github.com/jasonmlehman/circleoflicensing/blob/master/checklicensing.py and put it somewhere on your device.  i.e. c:\temp\checklicensing.py

4)  Create a json file that contains your office 365 application credentials

i.e c:\temp\o365cred.json

The content will look something like this:

{
        "clientid": "***************",
        "clientsecret": "******************",
        "loginurl": "https://login.microsoftonline.com/",
        "tenant": "yourtenantname.onmicrosoft.com",
        "tenant_guid": "your tenant guid"
}

If you don't have that info you can follow my instructions here to create it:  https://github.com/jasonmlehman/msgraphapi

5)  Update the checklicensing script and change this line to match where you saved the file above:

o365creds = 'path to json credential file'

Change to

o365creds = 'c:\\temp\\o365cred.json'

6)  Execute the python script: python c:\temp\checklicensing.py

7)  After that is created your CSV is generated with users that may not need enhanced licensing
