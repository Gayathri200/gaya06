x=int(input())
e=x-1
while(x>e):
  x=x-1
  r=map(int,input().split())
a=list(r) 
z=a[0]
print(a[0],a.index(z))
for i in range(a[0],a[x]):
  z=a[i]
  print(a[i],a.index(z))



