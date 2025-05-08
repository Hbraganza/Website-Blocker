# Website-Blocker
A website blocker that activates at certain hours that can be adjusted for different hours

**Please Note:**

**The file needs to be ran with Administration rights as it is editing the 'System32' file 'hosts'.
To find 'hosts' location follow this file path for Windows "C:/Windows/System32/drivers/etc/hosts". If you are not using windows please look up the file location.**

**<h2>ATTENTION</h2>
Microsoft does not recommend editing any files in 'System32' therefore use of this program is at your own risk and anything that happens is your responsibility, and therefore by using this code you are agreeing that you are solely liable if it damages anything.**

This is a python script that at set times will redirect set websites to your local IP giving a form resubmission error effectively blocking that website. These set time are 11pm to 6am and for Sunday night to Friday morning. It will block Facebook, Youtube and Netflix.

While the days it activates are more difficult to adjust, the time and website list can be adjusted easily when editing the program. To adjust the time the website blocker is placed, change the "Sleeptime" and "wake-up time" numbers depending on when you want the blocker to activate. Make sure the time is set up as shown in the program comment. If you are not using a value, set it to 0; otherwise, the program will not work.

To adjust the websites it blocks, simply write the URL of the desired website you want to block in between the square brackets between quotation marks and put a comma between each website URL, as shown in the code. It is important to separate each URL with commas, not quotation marks; otherwise, the hosts file will read that as one URL and not block the desired website.

For Windows: To automate the program's start-up when the computer is switched on, create a task on the task scheduler. In the General tab of the window that pops up, set the user to administrator or SYSTEM and tick the box to run with highest privileges. Then in triggers tab create a new trigger and set to activate upon switching on the computer. Under the actions tab create an action that starts a program then set the program location to where "Pyhton.exe" is, this is usually found in "C:\Program Files\Python37" or "\Python38" etc. depending on the version of Python that is used. Then on the add argument box give the location of the website blocker program. In the settings make sure to set not to start a new instance, as this program does not detect multiple instances of it running. The rest of the task setup is down to personal preference and the trigger tab can be adjusted to how you like

This was done with help from the following website:https://www.geeksforgeeks.org/website-blocker-using-python/
