a = int(input())
lst = [i for i in range(1, a+1) if a % i == 0]
print(*lst)