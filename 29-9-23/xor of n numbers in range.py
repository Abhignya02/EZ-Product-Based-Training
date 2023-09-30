#xor of n numbers in the range
#n=2 m=5 xor=2^3^4^5
#brute force O(n)
n=int(input("enter n"))
m=int(input("enter m"))
xor=0
for i in range(n,m+1):
    xor=xor^i
print(xor)
#optimal solution O(1)
n=int(input("enter n"))
m=int(input("enter m"))

