l1=list(map(int,input().split()))
l.sort()
print(l)
key=int(input())
high=len(l)-1
low=0
c=0
while(low<=high):
    mid=len(l)//2
    if(l[mid]==key):
        c+=1
        print("element found",mid+1)
        break
    elif(key>l[mid]):
        low=mid+1
    elif(key<l[mid]):
        high=mid-1
if c==0:
    print("element  not found")