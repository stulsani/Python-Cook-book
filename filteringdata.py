from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

print([n for n in mylist if n < 0])

print("Generator: ")

pos = (n for n in mylist if n < 0)

for x in pos:
    print(x)

#itertools.compress()
addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]

ans = list(compress(addresses,more5))

print(ans)
