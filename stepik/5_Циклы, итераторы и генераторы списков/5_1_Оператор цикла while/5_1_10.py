n, m = list(map(int,input().split()))
while n <= m:
    if n % 2 != 0:
        print(n, end = " ")
    n += 1
