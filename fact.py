t=int(input())
fact=1
if t==0:
  print(fact+t)
else:
  while(t>0):
    fact=fact*t
    t=t-1
  print(fact)
