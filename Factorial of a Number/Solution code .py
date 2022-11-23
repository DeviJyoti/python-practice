//LINK:-https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461392

        
def func(n):
    fact=1;
    if n<0:
        return "Error"
    elif n==0 or n==1:
        return 1 
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact

n=int(input())
print(str(func(n)))
