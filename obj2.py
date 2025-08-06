
def add():
    x=a+b
    print(x)
def sub():
    x=a+b 
    print(x) 
def mul():
    x=a*b
    print(x)
def div():
    x=a/b  
    print(x)

ch=int(input("enter ur choice"))

a=int(input("enter ur 1 st number"))
b=int(input("enter ur 2nd number"))

if(ch==1):
    add()
elif (ch==2):
    sub()
elif(ch==3):
    mul()
else:
    div()           


