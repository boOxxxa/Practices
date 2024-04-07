x = float(input())
ans = 0
for i in range(1, 10000000):
    ans += ((-1)**(1+i))*((x**i)/i)
print(round(ans, 8))