l=[]
n=int(input("enter size"))
for i in range(n):
    x=int(input())
    l=l+[x]
print(l)
for i in range(0,max(l)+2):
    if i  not in  l:
       print(i)
       break
    
    
