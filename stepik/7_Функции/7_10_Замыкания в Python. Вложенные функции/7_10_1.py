def counter_add():
    def add_sum(a):
        return a + 5
    return add_sum

cnt = counter_add()
k = int(input())

print(cnt(k))