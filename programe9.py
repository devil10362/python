from datetime import datetime as dt, timedelta

x=dt.today()  

print(x)

new_date =x + timedelta(12)
print ("new date time after addition of days to the current date")
print (new_date)  

