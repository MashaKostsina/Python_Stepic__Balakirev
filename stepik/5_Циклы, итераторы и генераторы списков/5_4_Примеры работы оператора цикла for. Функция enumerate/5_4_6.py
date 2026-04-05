num = list(map(float,input().split()))
minimum = []
for i in range(len(num)):
    if num[i] in num[1:-1] and num[i] < num[i+1] and num[i] < num[i-1]:
       minimum.append(num[i])
if len(minimum) == 1:
    if minimum[0] < num[0]:
        if minimum[0] < num[-1]:
            print(minimum[0])
        else:
            print(num[-1])
    else:
        if num[0] < num[-1]:
            print(num[0])
        else:
            print(num[-1])
else:
    print(minimum)


# n = list(map(float, input().split()))
#
# minimum = 0
#
# for i in range(len(n)):
#     if n[i - 1] > n[i]:
#         minimum = n[i]
#
# print(minimum)