def stringConstruction(s):
    return len(set(s))

t = int(input())
for _ in range(t):
    s = input().strip()
    print(stringConstruction(s))
