room = int(input())
index = room
tag = 1
while True:
    if index < 9:
        break
    index -= 8
    tag += 1
print(index, tag)