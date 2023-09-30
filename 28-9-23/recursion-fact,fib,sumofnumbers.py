n=int(input())
def add(n):
    if n<=0:
        return 0
    return n+add(n-1)
print("the sum of natural numbers ",add(n))
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print("the factorial of number ",fact(n))
n=int(input())
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("the fibinacii of number ",fib(n))