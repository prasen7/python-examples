# program to take input of starting hour and mins and duration(mins) and add duration(mins) to starting time.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
hour=hour+((dura+mins)//60)
mins=(dura+mins)%60
print("time of end of event "+str(hour)+":"+str(mins))