#1,2,3 digitnumber

x=int(input("enter the number"));

if(x<0):
    print("number is negative");
elif(x<10):
    print("number is single digit");
elif(x<100):
    print("number is double digit");
elif(x<1000):
    print("number is three digit");
else:
    print("number entry not in range");
    

