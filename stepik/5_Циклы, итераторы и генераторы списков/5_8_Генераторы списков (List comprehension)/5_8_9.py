a = input().split()
lst = [[a[i], int(a[i+1])] for i in range(0, len(a)-1, 2)]
print(lst)