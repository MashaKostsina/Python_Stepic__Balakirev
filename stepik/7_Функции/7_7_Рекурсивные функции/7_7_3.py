N = int(input())


# def fib_rec(N, f=[1, 1], index = 0):
#     if index == len(f):
#         return f
#     for i in range(2, N):
#         f.append(f[i-1] + f[i-2])
#
#     return f
def fib_rec(N, f=[1, 1]):
    return fib_rec(N, [*f, f[-1] + f[-2]]) if len(f) < N else f


print(fib_rec(N))

# def fib_rec(N, f=[1, 1]):
#     return fib_rec(N, [*f, f[-1] + f[-2]]) if len(f) < N else f
