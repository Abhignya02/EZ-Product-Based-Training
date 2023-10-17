"""
a 
b c 
d e f
"""
n=4
char=97
for i in range(n+1): 
    for j in range(i): 
        print(chr(char),end=" ")
        if char==122:
            char=96
        char+=1
    print()