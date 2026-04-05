def mergeSort(sort_nums):
    if len(sort_nums) > 1:
        mid = len(sort_nums) // 2
        lefthalf = sort_nums[:mid]
        righthalf = sort_nums[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                sort_nums[k] = lefthalf[i]
                i = i + 1
            else:
                sort_nums[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            sort_nums[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            sort_nums[k] = righthalf[j]
            j = j + 1
            k = k + 1


nums = list(map(int, input().split()))
mergeSort(nums)
print(nums)
