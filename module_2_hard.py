n = int(input())
result = []
for i in range(1, n):
    for j in range(i, n):
        if i > int(n / 2):
            break
        if n % (i + j) == 0 and i != j:
            result.append(i)
            result.append(j)
print(*result, sep= '')