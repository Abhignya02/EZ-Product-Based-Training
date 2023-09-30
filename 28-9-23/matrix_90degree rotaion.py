r=int(input("enter row"))
c=int(input("enter column"))
l=[]
for i in range(r):
    l1=[]
    for j in range(c):
        k=int(input())
        l1.append(k)
    l.append(l1)
print("original matrix")
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()
print("90 clock wise rotation")
for i in range(r):
    for j in range(c-1,-1,-1):
        print(l[j][i],end=" ")
    print()
print("90 anti clock wise rotation")
for i in range(r-1,-1,-1):
    for j in range(c):
        print(l[j][i],end=" ")
    print()


        