#space complexity of linear search is o(1)
a=list(map(int,input().split(" ")))
key=int(input("enter key"))
def linearsearch(a,key):
    c=0
    for i in range(len(a)):
        if a[i]==key:
            c+=1
            break
    if c>=1:
        print(key," element found")
    else:
        print(key," element not found")
        
linearsearch(a,key)

    