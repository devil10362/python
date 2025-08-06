#adding element in the list  [APPEND , EXTEND ,INSERT ,CONCATENATION]
b=[1,2,3,4,5,7,8,9,9];

#append is used for adding element in the last 
b.append(10);
print(b);
b.append("abc");

#insert is used for adding element on the particular index
b.insert(5,6);
print(b);

#extend is used to add iterable elements in the list and the last
b.extend("abc");
print(b);

#concatenation is used to add two add multiple list by using + operator
odd=[1,3,5];
even=[2,4,6];
num=odd+even;
print(num);