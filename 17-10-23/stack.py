stack=[]
stack.append(10)
stack.append(11)
stack.append(20)
stack.append(800)

print(stack.pop())
print(stack.pop())
if len(stack)!=0:
    print("top of stack",stack[-1])
