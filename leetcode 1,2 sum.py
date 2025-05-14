l=list(map(int,input().split()))
t=int(input())
s={}
for i in range(len(l)):
    if t-l[i] in s:
        print([s[t-l[i]],i])
        break
    s[l[i]]=i