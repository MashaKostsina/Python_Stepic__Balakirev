digs = list(map(int,input().split()))
def get_mult(a, b):
    return a * b


print(get_mult(min(digs), max(digs)))