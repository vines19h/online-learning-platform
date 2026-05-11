n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = float('inf')
    for d in str(i):
        dp[i] = min(dp[i], dp[i - int(d)] + 1)

print(dp[n])
