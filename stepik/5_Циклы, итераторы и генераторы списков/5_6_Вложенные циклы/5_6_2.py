lst_in = ["django chto  eto takoe    poryadok ustanovki",
     "model mtv   marshrutizaciya funkcii  predstavleniya",
     "marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya"
     ]

for row, line in enumerate(lst_in):
    while line.count('  '):
        line = line.replace('  ', ' ')
    while line.count(' '):
        line = line.replace(' ', '-')
    lst_in[row] = line

print(*lst_in, sep="\n")
