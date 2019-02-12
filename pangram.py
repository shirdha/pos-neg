n=input()
a={}
for i in range(97,123):
    a.update({chr(i):0})
n=n.lower()
n=n.replace(" ","")
c=0
for j in n:
    s=n.count(j)
    a.update({j:s})
for x,y in a.items():
    if y>=1:
        c=c+1
if c==26:
    print("yes")
else:
    print("no")
