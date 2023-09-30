#swaping numbers using XOR
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a,b)
#swaping numbers using third var
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a,b)
#swaping numbers without using var
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a,b)