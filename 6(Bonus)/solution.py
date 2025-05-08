a, b = map(int, input().split())
Digits = [i for i in range(1, a+1)]
Lost = []
i = 0
while len(Digits) > 1:
    i = (i + b - 1) % len(Digits)
    x = Digits.pop(i)
    Lost.append(x)
Lost.append(Digits[0])
print(' '.join(map(str, Lost)))