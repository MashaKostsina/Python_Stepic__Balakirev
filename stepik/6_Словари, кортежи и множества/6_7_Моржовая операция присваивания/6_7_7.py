#Продолжите программу, в которой уже объявлена функция f и формируется кортеж t:
def f(x):
    return abs(x) ** 0.5 + 3.2 + x


t = tuple(map(float, input().split()))  # кортеж t в программе не менять

lst = [[x := f(i), x**2, x**3] for i in t]

for i in lst:
    print(*i)