#check the given number is power of 2
#tc:O(logn)
#for all power of 2 values there will be only one set bit n=4(100) n=8(1000) n=16(10000)
n=5
count=0
while(n):
    if n&1==1:
        count+=1
    n=n>>1
if count==1:
    print("power of 2")
else:
    print("not power of 2")