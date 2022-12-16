"""Program 3. Create a list L=[10,20,30]. Write program
to perform followimng operations
a. insert new num ber to list L
b. Delete numbers from list L
c. Sum of all numbers in list L
d. Sum of all prime numbers in list L
e. Delete the list L."""

#program for performing operations on list
#1. INSERTION :-
list = [10,12,13]
print("the original list is : ",list)
list.append(14) #ppend the element at the ebnd of list
list.insert(2,22) # insert at the particular postion in list
list.extend((23,24,25)) ## extending string elements
print("list after insertion : ", list)
#2. DELETION :-
list1 = [10,12,13,14,15]
print("the original list is : ",list1)
list1.remove(10)
list1.remove(15)
print("list after deltion :- ",list1)
#3. SUM OF ALL NUMBERS OF LIST
list = [1,2,3,4,5,6,7,8]
sum=0;
for x in list:
sum=sum+x
print("sum of elements of list is :- ",sum)
#4.sum of all prime numbers of list
list=[1,2,3,4,5,6,7]
prime=[]
for i in list:
c=0
for j in range(1,i):if i%j==0:
c+=1
if c==1:
prime.append(i)
s=0
for x in prime:
s+=x
print("sum of all primes is :- ",s)
#5. delte list
del list
print("list is deleted successfully....")
