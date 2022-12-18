numbers = [5, 3, 1, 2, 4]
n = len (numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if (numbers[j]>numbers[j+1]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in numbers:
    print(i)