n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = arr[i]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        dp[l][r] = max(arr[l] - dp[l + 1][r], arr[r] - dp[l][r - 1])

# total_score = (sum(arr) + d_
