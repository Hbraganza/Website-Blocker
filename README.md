# Website-Blocker
A website blocker that activates at certain hours that can be adjusted for different hours

**Please Note:**

**The file needs to be ran with Administration rights as it is editing the 'System32' file 'hosts'.
To find 'hosts' location follow this file path for Windows "C:/Windows/System32/drivers/etc/hosts". If you are not using windows please look up the file location.**

**<h2>ATTENTION</h2>
Microsoft does not recommend editing any files in 'System32' therefore use of this program is at your own risk and anything that happens is not my fault.**

This is a python script that at set times will redirect set websites to your local IP giving a form resubmission error effectively blocking that website.

For Windows: To automate starting the program when the computer is started up, make a task on task scheduler. In the General tab of the window that pops up, set the user to adminstrator or SYSTEM and tick the box to run with highest privileges. Then in triggers tab create a new trigger and set to activate upon switching on the computer. Under the actions tab create an action that starts a program then set the program location to where "Pyhton.exe" is, this is usually found in C:\Program Files\Python37 or \Python38 etc. depending on the version of Python that is used. Then on the add argument box give the location of the website blocker program. In the settings make sure to set not to start a new instance, as this program does not detect multiple instances of it running.  

This was done with help from the following website:https://www.geeksforgeeks.org/website-blocker-using-python/
