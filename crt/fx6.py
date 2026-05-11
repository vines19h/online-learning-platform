n, x = map(int, input().split())
arr = list(map(int, input().split()))

# store values with original index
vals = [(arr[i], i + 1) for i in range(n)]
vals.sort()  # sort by values

for i in range(n):
    a = vals[i][0]
    target = x - a
    l = i + 1
    r = n - 1

    while l < r
