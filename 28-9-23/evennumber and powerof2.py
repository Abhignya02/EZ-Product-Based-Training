n1=int(input("enter range"))
n2=int(input("enter range"))
s=int(input("enter size"))
l=[]
for i in range(s):
    k=int(input())
    if k>=n1  and k<n2:
        l.append(k)
    else:
        print("enter num in range")
        k=int(input())
        l.append(k)   
print("even numbers")
l2=[]
for i in l:
    if i%2==0:
        l2.append(i)
        print(i,end=" ")

print("\n2 power values")
for i in l:
    for j in range(0,max(l2)):
        if(2**j==i):
           print(i)

