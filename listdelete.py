#deleting elements from list by REMOVE,POP 
a=[1,2,3,4,5,6,7,8,9,9];
print(a,"\n");

#remove() deletes the first matching value in the given list
a.remove(9);
print (a);

#pop() is used to delete the elements on the particular index and also return the poped value from the list
element=a.pop(-1);
print(element);
print(a);





