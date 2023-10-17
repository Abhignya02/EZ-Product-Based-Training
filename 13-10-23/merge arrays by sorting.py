arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
i=0
j=0
ans=[]
'''
while i<len(arr1) or j<len(arr2):
    if i<len(arr1):
        while j<len(arr2):
            ans.append(arr2[j])
            j+=1
    elif j<len(arr2):
        while i<len(arr1):
            ans.append(arr1[i])
            i+=1
    elif arr1[i]<arr2[j]:
        ans.append(arr1[i])
        i+=1
    else:
        ans.append(arr2[j])
print(ans)'''
while i < len(arr1) and j < len(arr2):
    
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
        ans.append(arr2[j])
        j += 1
   
    while i < len(arr1):
            ans.append(arr1[i])
            i += 1
    while j < len(arr2):
            ans.append(arr2[j])
            j += 1
print(ans)

