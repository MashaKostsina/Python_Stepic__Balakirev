number = list(map(float,input().split()))
cities = input().split()
lst = [*number, *cities]
print(*lst)