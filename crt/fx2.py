import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
it = iter(data)
n = int(next(it))
x = int(next(it))
arr = [int(next(it)) for _ in range(n)]


pairs = [(arr[i], i) for i in range(n)]
pairs.sort() 

for i in range(n-2):
    target = x - pairs[i][0]
    l, r = i+1, n-1
    while l < r:
        s = pairs[l][0] + pairs[r][0]
        if s == target:
        
            print(pairs[i][1] + 1, pairs[l][1] + 1, pairs[r][1] + 1)
            sys.exit(0)
        elif s < target:
            l += 1
        else:
            r -= 1

print("IMPOSSIBLE")
