n = int(input())
a = list(map(int, input().split()))
total = sum(a)

found = False
for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            x, y = a[i], a[j]
            if x <= y and x + 2 * y == total:
                print(x, y)
                found = True
                break
    if found:
        break