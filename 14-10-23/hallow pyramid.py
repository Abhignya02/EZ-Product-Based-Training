'''
        1         
      1   2       
    1       3     
  1           4   
1   2   3   4   5
'''
n=5
start=n-1
end=n-1
var=2
flag=0
for i in range(n):
    for j in range(2*n-1):
        if j==start:
            print("*",end=" ")
        elif j==end:
            print("*",end=" ")
        elif i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    start-=1
    end+=1
