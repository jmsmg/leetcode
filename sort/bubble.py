n = list(map(int, input().split()))

for idx in range(len(n)-1):
    for i in range(len(n) - idx - 1):
        if n[i] > n[i+1]:
            n[i], n[i+1] = n[i+1], n[i]

print(n)
