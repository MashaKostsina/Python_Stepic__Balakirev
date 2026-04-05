def is_even(a):
    return True if a % 2 == 0 else False

x = int(input())
while x != 1:
    if is_even(x):
        print(x)
    x = int(input())
