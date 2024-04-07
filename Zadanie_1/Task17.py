w = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
pol = input()
colors = ['black', 'white']
if w.index(pol[0]) % 2:
    color = colors[w.index(pol[0]) % 2]
    tag = 1
else:
    color = 'black'
    tag = 2
item = int(pol[1])

for i in range(1, item):
    tag = abs(tag-1)
    color = colors[tag]
print(color)