n = int(input())
lst = [1, 1]
i = 0
while len(lst) < n:
    lst.append(lst[i] + lst[i+1])
    i +=1
print(*lst)

