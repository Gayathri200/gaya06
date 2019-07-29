x=map(int,input().split())
y=map(int,input().split())
c=list(x)
d=list(y)
e=c[0]-d[0]
f=c[1]-d[1]
if(e<0 and f<0):
  print(-e,-f) 
else:
  print(e,f)
  
