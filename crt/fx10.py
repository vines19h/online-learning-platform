def runningTime(arr):
    shifts = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # shift larger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1

        arr[j + 1] = key   # final placement of key

    return shifts


# Input handling (for HackerRank style)
n = int(input())
arr = list(map(int, input().split()))
print(runningTime(arr))
