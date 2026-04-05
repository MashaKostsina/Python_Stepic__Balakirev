number = list(map(int,input().split()))
summ = 0
for i in range(len(number)):
    if number[i] % 2 != 0:
        summ += number[i]
print(summ)
