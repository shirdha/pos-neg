#shirdha
def pro(n):
    for i in range(1,n+1):
        if (2**i)==n:
            return True
def pow1(n):
    a=0
    for j in range(1,n+1):
        if pro(j):
            a=j
    return a

n=int(input())
if pro(n):
    print("0")
else:
    a=pow1(n)
    print(n-a)
   
