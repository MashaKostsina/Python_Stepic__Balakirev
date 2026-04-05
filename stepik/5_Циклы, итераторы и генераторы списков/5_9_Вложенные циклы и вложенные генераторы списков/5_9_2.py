lst = list(map(int,input().split()))
a = int(len(lst)**0.5)
b = [lst[i:i+a] for i in range(0, len(lst), a)]
print(b)