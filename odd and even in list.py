l=[3,2,6,4,1,5,7]
l.sort()
res=[]
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)