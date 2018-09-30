g=int(input(" "))
e=0
f=1
count=0
if(g==0):
  print(e)
elif(g<0):
  print("positive number")
else:
  while(count<g):
    print(e)
    nexterm=e+f
    e=f
    f=nexterm
    count+=1
