n=list(map(int,input().split(" ")))
for i in range(len(n)):
    count=0
    for j in range(len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            count+=1
    if count==0:
        break
print(n)
            

       