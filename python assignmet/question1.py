import math
# a. find maximum of list
print("\nPROGRAM 1.a-->")
# Declaring a list with random integers.
list1 = [4, -4, 8, -9, 1]

# Store maximum value in a variable
# using Python list max() function.
maxValue = max(list1)

# Printing value stored in maxValue.

print(maxValue)

#b. GCD of two numbers
# math module contains the gcd function

print("\nPROGRAM 1.b-->")
# now, let's calculate the gcd of 2 numbers.
print("enter two numbers you want to calculate gcd : ")
x = int(input("enter first number : "))
y = int(input("enter second number : "))
hcf = math.gcd(x,y)

print(f"The GCD of {x} and {y} is {hcf}.")

#c. SQUARE ROOT OF A NUMBER
print("\nPROGRAM 1.c-->")
number = int(input("enter the number : "))
sqrtOfNumber = math.sqrt(number)
print('square root of number entered: ', sqrtOfNumber)

#d CHECK A NUMBER IS PRIME OR N0T
print("\nPROGRAM 1.d-->")

num = int(input("enter the number : "))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#e. PRINT FIRST N PRIME NUMBERS

print("\nPROGRAM 1.e-->")

numr=int(input("Enter range:"))

print("Prime numbers:",end=' ')

for n in range(1,numr):

    for i in range(2,n):

        if(n%i==0):

            break
    else:

        print(n,end=' ')

#f. REMOVE DUPLICATE FROM THE LIST

print("\nPROGRAM 1.f-->")

# Python 3 code to demonstrate
# removing duplicated from list
# using set()

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))

# using set()
# to remove duplicated
# from list
test_list = list(set(test_list))

# printing list after removal
# distorted ordering
print("The list after removing duplicates : "
      + str(test_list))


#1.g PRINT FIBPNACCI SERIES
print("PROGRAM 1.g-->")
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("enter the number of terms :- "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1," ",end=' ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

