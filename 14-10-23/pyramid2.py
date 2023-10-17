"""
   *
  * *
 * * *
* * * *
"""
n=int(input())
row=n
col=2*n-1
start,last=n-1,n-1
mid = start
for i in range(row):
    for j in range(col):
        if j>=start and j<=mid:
            print("* ",end='')
        else:
            print(" ",end='')
    print()
    start-=1
    last+=1