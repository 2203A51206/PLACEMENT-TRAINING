arr=[12,11,13,5,6]
for i in range(1,len(arr)):
    k=arr[i]
    j=i-1
    while j>=0 and arr[j]>k:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=k
print(arr)