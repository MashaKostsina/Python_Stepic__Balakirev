def show_numbers(num_list):
    min_num = min(num_list)
    max_num = max(num_list)
    sum_num = sum(num_list)
    print(f'Min = {min_num}, max = {max_num}, sum = {sum_num}')


show_numbers(num_list=[int(x) for x in input().split()])