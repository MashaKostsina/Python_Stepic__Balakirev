import sys


def is_isolate(*args,i,j) :
    summa = 0
    for k in range(0,2) :
        summa += args[i][j + k] + args[i + 1][j + k]
    if summa <= 1 :
        return True
    else :
        return False


def verify(*args) :
    args = list(*args)
    n = len(args)
    for x in range(n - 1) :
        for y in range(len(args[x]) - 1) :
            if not is_isolate(*args,i = x,j = y) :
                return False
    return True


# lines = sys.stdin.readlines()
# lst2D = [[int(y) for y in x.split()] for x in lines]
lst2D = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
print(verify(lst2D))