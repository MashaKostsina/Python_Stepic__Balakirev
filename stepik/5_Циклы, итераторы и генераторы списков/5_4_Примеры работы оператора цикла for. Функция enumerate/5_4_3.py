num = input()
num = num.replace(' ', '').replace('+', ' +').replace('-', ' -')
num = list(map(int, num.split()))
print(sum(num))
