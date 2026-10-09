n, k = map(int, input().split())
time = 240 - k
count = 0
for i in range(1, n + 1):
    time -= 5 * i
    if time < 0:
        break
    count += 1
print(count)