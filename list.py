
#single dimension list / list
x=[1,2,3,4,5,6];
print(x);
print(x[0]);
print(len(x));


#multidimension list
x=[[1,2,3,4],["a","b","c","d","e"]];
print(x);
print(x[0][1]);

#taking list from user
b=(input("enter the size of list"))
for i in b:
    list=input("enter the elements of list\n");
    a=list.split();
    
    
print("the list is\t",a);

