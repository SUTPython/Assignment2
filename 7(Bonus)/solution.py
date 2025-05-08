lst = [(num, i) for i, num in enumerate(map(int, input().split()))]

sum = int(input())

lst.sort(key=lambda x: x[0])

pointer1 = 0
pointer2 = len(lst) - 1

result = []
while pointer1 < pointer2:
    if lst[pointer1][0] + lst[pointer2][0] == sum:
        result.append(lst[pointer1][1] + lst[pointer2][1])
        pointer1 += 1
        pointer2 -= 1

    elif lst[pointer1][0] + lst[pointer2][0] > sum:
        pointer2 -= 1

    elif lst[pointer1][0] + lst[pointer2][0] < sum:
        pointer1 += 1


result.sort()

if len(result) == 0:
    print('Not Found!')

[print(i) for i in result]