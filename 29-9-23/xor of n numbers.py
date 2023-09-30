#input=5   then calculate (1^2^3^4^5)=1

#brute force  O(n)
n=int(input())
xor=0
for i in range(1,n+1):
    xor=xor^i
print(xor)
#optimal solution  O(1)
n=int(input())
xor=0
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)
