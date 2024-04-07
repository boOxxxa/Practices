def par(*args):
    item = 1
    for i in args:
        item *= i
    return item


print(par(2, 3, 4))
print(par(2, 3))