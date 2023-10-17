n=4
start=n-1
end=n-1
for i in range(n):
    for j in range(2*n-1):
        if j>=start and j<=end:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    start-=1
    end+=1
for i in range(n):
    print("  "*(n-1-i)+"* "*i+"* "+"* "*(i))