n = 40

first = 1
second = 2

for i in range (4,41):
    ans = first + second
    first = second
    second = ans

print(ans)
