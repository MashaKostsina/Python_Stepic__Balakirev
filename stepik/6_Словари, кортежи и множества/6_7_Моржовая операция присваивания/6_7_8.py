product = 1
while (x := int(input())) > 0:
    if x % 3 == 0:
        product *=x
print(product)