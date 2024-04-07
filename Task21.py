x=[1,3,4,7,8,9,10]
g=[]
for i in range(1,len(x)):
    g.append((x[i]-x[i-1])/0.01)
print(max(g))