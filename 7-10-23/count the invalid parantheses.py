s=input()
stack=[]
c=0
for i in s:
        if i=='[' or i=='{' or i=='(':
            stack.append(i)
            c+=1
        else:
            if (i=='}' and stack[-1]=='{') or( i==')' and stack[-1]=='(' ) or( i==']' and stack[-1]=='[' ):
                stack.pop()    
                c+=1
if  len(stack)==0:
    print(0)
elif c>=1 or len(stack)!=0 :
    print(c+1)
    print(" not balanced")


