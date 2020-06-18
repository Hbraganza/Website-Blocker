import time
from datetime import datetime as dt

hosts_path="C:/Windows/System32/drivers/etc/hosts"
#Requires admin rights to run as it is a system32 folder being tampered with

redirect="127.0.0.1"#Redirecting to local IP address
#To block website write in this format ["websiteurl1","websiteurl2",...,"websiteurln"]
website_list =["www.facebook.com","facebook.com","www.youtube.com",
               "youtube.com","www.manganelo.com","manganelo.com",
               "m.manganelo.com","www.manganelo.com","mangakakalot.com",
               "www.netflix.com","netflix.com"] 
d =24*60*60
h =60*60

#adjustable times [hours,minutes,seconds,microseconds]
Sleeptime=[23,0,0,0]#when the blocker switches on
wakeuptime=[6,0,0,0]#when the blocker switches off

while True:

    T=dt.now()#Taking current time
    WD=T.weekday()#Taking the weekday as a value from 0-6 where 0 = monday and 6 = sunday
    upb=T.replace(hour=int(Sleeptime[0]),
                  minute=int(Sleeptime[1]),
                  second=int(Sleeptime[2]),
                  microsecond=int(Sleeptime[3]))#replacting current time but keeping current date
    lpb=upb.replace(hour=int(wakeuptime[0]),
                    minute=int(wakeuptime[1]),
                    second=int(wakeuptime[2]),
                    microsecond=int(wakeuptime[3]))
    supb=upb.replace(hour=int(Sleeptime[0])-1)
    slpb=lpb.replace(hour=int(wakeuptime[0])-1)
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

