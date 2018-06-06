lst = {1: [' ', '|', ' ', '|', ' '], 'first': ['- -', '- -', '- '], 2: [' ', '|', ' ', '|', ' '],
       'second': ['- -', '- -', '- '],
       3: [' ', '|', ' ', '|', ' ']}
for i in lst:
    for n in range(0, len(lst[i])):
        print(lst[i][n], end=' ')
    print()
