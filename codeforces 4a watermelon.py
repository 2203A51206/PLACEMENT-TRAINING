w=int(input("enter the weight of the watermelon:"))
if w%2!=0:
    print("no")
else:
    x=w//2
    if(x%2==0):
        print(x,x)
    else:
        print(x-1,x+1)