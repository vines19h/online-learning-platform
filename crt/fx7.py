n, x = map(int, input().split())
arr = list(map(int, input().split()))

from collections import defaultdict
count = defaultdict(int)
count[0] = 1  # prefix sum 0 appears once

prefix = 0
ans = 0

for num in arr:
    prefix += num
    ans += count[prefix - x]   # how many times needed prefix existed
    count[prefix] += 1

print(ans)
