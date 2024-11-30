def rec(n):
    if n == 1:
        return 1
    return n * rec(n - 1)


t = int(input())
for i in range(t):
    n = int(input())
    print(rec(n))
