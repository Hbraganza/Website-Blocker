#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from datetime import datetime as dt

hosts_path="C:/Windows/System32/drivers/etc/hosts"
#Requires admin rights to run as it is a system32 folder being tampered with

redirect="127.0.0.1"#Redicting to local IP address

website_list =["www.facebook.com","facebook.com","www.youtube.com",
               "youtube.com","www.manganelo.com","manganelo.com","m.manganelo.com","www.manganelo.com",
               "mangakakalot.com","www.netflix.com","netflix.com"] 
d = 24*60*60
h =60*60

Sleeptime= 23#adjustable times to blockwebsites
wakeuptime= 6

while True:

    T=dt.now()#Taking current time
    WD=T.weekday()#Taking the weekday as a value from 0-6 where 0 = monday and 6 = sunday
    upb=T.replace(hour=Sleeptime,minute=0,second=0,microsecond=0)#replacting current time but keeping current date
    lpb=upb.replace(hour=wakeuptime)
    supb=upb.replace(hour=Sleeptime-1)
    slpb=lpb.replace(hour=wakeuptime-1)
    t=T.time
    
    if (upb<T or T<lpb) and (0<=WD<=3 or WD==6 or(WD==4 and T<lpb))and not(T<lpb and WD==6):
        print("Sleeping hours...") 
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list: 
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
            file.close()
    else: 
        with open(hosts_path, 'r+') as file:
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line)
            file.truncate()
            file.close()
  
        print("Fun hours...")
        
    if ((upb<T or T<slpb) and (0<=WD<=3 or WD==6 or(WD==4 and T<slpb))and not(T<lpb and WD==6))or(lpb<T<supb and(0<=WD<=3 or WD==6)):
        time.sleep(h)#make sure it is not spam printing and using up processing power

    elif 4<=WD<=5:
        time.sleep(d)
    
    else:
        time.sleep(5)

