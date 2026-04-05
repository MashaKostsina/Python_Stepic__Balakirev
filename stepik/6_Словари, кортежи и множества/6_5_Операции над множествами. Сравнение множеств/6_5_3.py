list_1 = list(map(int,input().split()))
list_2 = list(map(int,input().split()))
s1 = set(list_1)
s2 = set(list_2)
s = s1 ^ s2
print(*sorted(s))