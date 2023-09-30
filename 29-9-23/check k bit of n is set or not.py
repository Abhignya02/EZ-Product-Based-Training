#for the given number n,check kth bit is set or not
#means whether the pos of the n is 1 or not
n=int(input("enter num"))
k=int(input("enter pos"))
m=n&(1<<k-1)
if m>=1:
    print("set")
else:
    print("not set")