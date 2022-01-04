# tos-alert
A discord bot providing notifications of player activity on a minecraft server.

Setup
By default the app does not launch and will crash with the error ``` UnchangedDefaults ```, you must input your values to the configuration file as described below:
```
[SETUP]
rate=60 #time in seconds between refresh cycles

[DISCORD]
token=None #token for the Discord Develop API
channelID=None #channel for the bot to display updates to

[MINECRAFT]
serverIP=None #ip address of the target server
playersOfInterest=[] #a python formatted list of user in game names, exact ign only. TODO: search by UUID?
```
