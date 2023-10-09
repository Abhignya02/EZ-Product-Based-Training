n=input()
s=""
for i in range(len(n)):
    if (n[i]>='a' and n[i]<='z') or (n[i]>='A' and n[i]<='Z') or(n[i]>='0' and n[i]<='9'):
        s+=n[i]
    else:
        p=i
        q=n[i]
s=s[::-1]
s=list(s)
print(s)
r=""
for i in range(p):
    r+=s[i]
r+=q
for i in range(p,len(s)):
    r+=s[i]
print(r)

        