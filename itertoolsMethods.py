from itertools import chain

a = [3,4,5,6,7]
b = [10,20,30,40]

for i in chain(a,b):
    print(i)
