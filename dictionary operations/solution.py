"""Program 4. Create a Dictionary
D={‘name’:’allen’,’age’:27,5:123456}. Write program to
perform following operations :
a. insert new entry in D
b. delete an entry from D
c. check whether a key is present or not
d. update the values of a key
e. clear dictionary D
"""

CODE:-
#program 12. perform operations on dictionary
D={'Name':'Allen','Age':27,5:123456,'class':'cse','address':'Hisar','p
hone_no':9992343507}
print("Original Dictionary :- ",D)
#1. insert new entity in D
print("insert new entity in D :- ")
D['roll_no']=200010130051
print("Dictionary after insertion :- ",D)
#2.delet an entry from D
print("\ndeletion from D :- ")
D.pop('Age') #removes the item with the specified key name:
print("Dictionary after deletion :- ",D)
D.popitem() # removes the last inserted item
print("Dictionary after deletion :- ",D)
#3.check whether key is pre4sent or not in D
print("\ncheck whether key is pre4sent or not in D")
if 'Name' in D:
print("key is present")
else:
print("key is not present")
#.4 update the key values
print("\nupdate key values of D :- ")
D.update({'address':'GJU'})
D.update({"Age": 19})print("Dictionary after updation :- ",D)
#5. clear D :-
print("\nclear D :- ")
D.clear()
print("Dictionary is cleared successfully....")
