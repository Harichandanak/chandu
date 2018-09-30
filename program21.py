N,A,D=map(int,input().split())
sum1=0
for k in range(N):
  sum1=sum1+A
  A=A+D
  k=k+1
print (sum1)
