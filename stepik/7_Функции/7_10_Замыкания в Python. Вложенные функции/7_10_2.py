def counter_add(n):
    def new_counter(a):
        nonlocal n
        return a + n

    return new_counter


cnt = counter_add(2)
k = int(input())
print(cnt(k))
