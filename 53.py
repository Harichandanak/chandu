N=int(input(" "))
t=0
while(N>0):
  e=N%10
  t=t+e
  N=N//10
print(t)
