k=int(input())
a=[]
for i in range(1,k+1):
    b=list(map(int,input().split()))
    a=a+b
a.sort()
for i in range(len(a)):
    if i==len(a)-1:
        print(a[i],end="")
    else:
        print(a[i],end=" ")
