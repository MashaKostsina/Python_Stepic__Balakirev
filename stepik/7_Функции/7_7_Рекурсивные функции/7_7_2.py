a = list(map(int, input().split()))


def get_rec_sum(a, sum=0):
    for i in a:
        sum += i
    print(sum)


get_rec_sum(a)

# def get_rec_sum(nums, index=0, summa=0):
#     '''Рекурсивная функция вычисляет сумму чисел из введенного списка'''
#     if index >= len(nums):
#         return summa
#     return get_rec_sum(nums, index+1, summa+nums[index])
#
#
# nums = list(map(int,input().split()))
# print(get_rec_sum(nums))
