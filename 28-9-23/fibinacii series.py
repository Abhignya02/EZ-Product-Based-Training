n=int(input())
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("the fibinacii of number ",fib(n))
n=int(input())
f=0
s=1
for i in range(0,n+1):
    # to print series print(f)
    n=f+s
    f=s
    s=n
print(s)
    
               

