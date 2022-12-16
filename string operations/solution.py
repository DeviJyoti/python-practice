"""Program 2. To perform various on string like creation,deletion
and concatination."""

#CODE:-
#program 10.
#1. String creation
a = "Hello"
print(a)
#multiline string:-
b="""hello,Iam Jyoti and i am a student of GJU.
I love coding"""
print(b)
#ieration
print(a[3])
for i in range(6):
print(b[i])
print(len(a)) # string length
#2. String Concatenation
a="hello"
b="i am jyoti"
c=a+b
print(c)
print(a+" "+b)
#3. deletion from string
print(a.replace('h',''))
print(b.replace('i',''))
print(a.translate({ord('l'): None}))
