a, b, c, d = [int(x) for x in input().split()]

add = a * b * c * d

if add < 99:
    print(f"{add:02d}")
else:
    print(f"{(add % 100):02d}")
