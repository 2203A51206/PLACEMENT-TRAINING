m=[[1,2,3],
   [4,5,6],
   [7,8,9],
   ]
rows=len(m)
cols=len(m[0])

for row in m:
    print(row)
for i in range(rows):
    for j in range(cols):
            n=m[i][j]
            if n>1:
                is_prime=True
                for k in range(2,n):
                    if n%k==0:
                        is_prime=False
                        break
                if is_prime:
                    print(n)