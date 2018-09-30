g,h=input().split(' ')
g,h=int(g),int(h)
g = g ^ h;
h = g ^ h;
g = g ^ h;
print(g,h)
