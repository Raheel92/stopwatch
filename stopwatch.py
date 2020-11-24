from time import localtime, mktime, strftime

#Start timer
start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

#Ask user to stop timer
input("Press 'Enter' to stop timer ")

#Stop timer
stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print (f"Timer stopped at {strftime( '%X', stop_time)}")
print (f"Total time: {difference} seconds")