l=list(map(int,input().split()))
key=int(input())
c=0
for i in range(len(l)):
    if l[i]==key:
        c+=1
        print(key," is at index ",i)
        break  
if c==0:
    print("elemnt not found")
    