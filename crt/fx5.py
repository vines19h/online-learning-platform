t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    m = max(y, x)

    if m % 2 == 0:  # even layer
        if y == m:
            print(m*m - x + 1)
        else:
            print((m-1)*(m-1) + y)
    else:  # odd layer
        if x == m:
            print(m*m - y + 1)
        else:
            print((m-1)*(m-1) + x)
