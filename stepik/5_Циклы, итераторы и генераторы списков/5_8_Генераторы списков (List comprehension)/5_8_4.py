a = input().split()
cities = [i for i in a if len(i) > 5]
print(*cities)