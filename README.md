# Free'ing up Microsoft licenses!

Busineses that use Office 365 often have various levels of Microsoft licenses that may include standard and enhanced licenses.  For example, let's say you're in manufacturing and you have users that only need a Kiosk license or even an office only (F3/E1, etc) license.  These licenses are MUCH cheaper than the Microsoft enhanced licenses like E3/E5.  Often times businesses find themselves in a position where they have an astronomical bill when it's time to true up licenses.  

Why does this happen?  Most place don't have a solid licensing provision process and users find ways to get the enhanced licenses even though they don't need them.  Well, if you want to save your business a ton of money come true up time then I'd be glad to help, and so will this job.  This job servers as a tacticle response to the ballooning of enhanced licenses.  To make this work long term you would need a special process designed specifically for your organization.  I call it "The circle of Licensing."  With automation we can see if the enhanced license has been consumed by a user that it is assigned to.  If it hasn't been used, then that user gets downgraded to the standard license.  You will need a solid request process for the user to re-request the enhanced license.

I could do this in powershell as well, I just choose not to.

# Installation

You will need my msgraphapi.  Follow the instructions to setup your connection below.

* pip install git+https://github.com/jasonmlehman/msgraphapi.git

# How?

Glad you asked.  How do I determine if a user is using a license or not?  Think about the SKU's and what is really determing if a user is using that SKU.  A simple comparison would be an F3 and an E3 user.  The only "real" difference is whether that user has activated office Pro Plus.  If they aren't using Office Pro Plus why do they have the license?  Mobile, Teams, Onedrive are no different between the SKU's.  So, if we can determine who has activiated Office pro plus within a specified time period then we can assume that user doesn't need enhanced licensing.

