h=input()
n=0
for i in h:
  if(i>='A' and i<='Z' or i>='a' and i<='z' or i.isdigit()):
    a=3
  else:
    n+=1
print(n)
