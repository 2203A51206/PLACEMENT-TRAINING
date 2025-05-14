def fun(n):
    if n==00:
        return 200
    print(n,end=" ")
    t=fun(n-1)
    return 200
n=5
print(fun(n))

