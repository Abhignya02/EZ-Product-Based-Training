l=list(map(int,input().split(",")))
s=0
n1=l.index(4)
n2=l.index(7)
for i in range(0,n1):
    s+=l[i]
for i in range(n2+1,len(l)):
    s+=l[i]
print(s)
st=""
l2=[]
for i in range(n1,n2+1):
    l2.append(str(l[i]))
for i in l2:
    st+=i
print(st)
print(s+int(st))