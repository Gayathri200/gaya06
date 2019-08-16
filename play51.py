x=int(input())
a=map(int,input().split())
b=list(a)
g=sorted(b)
t=len(g)
if(t==x):
  print(g[1])
