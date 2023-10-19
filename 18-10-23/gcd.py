m=6
n=5
ans=1
for i in range(2,n+1):
    if m%i==0 and n%i==0:
        ans=i
print(ans)