x, y = map(float, input().split())
a = (x-1)**2+y**2 <= 4 and (x-1)**2+y**2 >= 1
b = abs(x-4) < 2 and abs(y-2) < 3
if a and b:
    print('yes yes')
elif b and not a:
    print('no yes')
elif a and not b:
    print('yes no')
else:
    print('no no')