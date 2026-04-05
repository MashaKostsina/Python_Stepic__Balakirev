a = list(map(float,input().split()))
lst = [i for i in a if a.index(i) % 2 == 0]
print(*lst)