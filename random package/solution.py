"""two assigment on usage of different
available packeges like random package to perform
a. Print N random numbers ranging from 100 to 500
b. Print 10 random strings whose length between 3 and
5.
"""
CODE :-
#program 17
#a. print N random numbers ranging from 100 to 500
import random
import string
# printing a random number
num1 = random.randint(100, 500)
print("an random number in range of 100 to 1000 :-",num1)
# printing n random numbers
for i in range(5):
print(random.randint(100,500),end=' ')
# random number with step 2 in a given range :-
num2 = random.randrange(1000, 10000, 2)
print("\n\nan random number with step 2 in range of 1000 to
2000 :-",num2)
#b. print 10 random strings whose length between 3 and 5
print("10 random strings whose length between 3 and 5 ")
def randStr(chars = string.ascii_uppercase + string.digits,N=10):
return ''.join(random.choice(chars) for _ in range(3,6))
for i in range(10):
print(randStr())
