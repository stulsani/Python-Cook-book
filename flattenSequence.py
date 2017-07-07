from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):
            yield from flatten(i)
        else:
            yield i


listA = [1,2,[3],[4,5],[6,7],8,[9,10]]
listB = ["Sumeet", "Tulsani", "Sagar", "Tulsani", [4,7], "Kapil"]

print("Result from List A: ")
for item in flatten(listA):
    print(item)

print("Result from List B: ")
for item in flatten(listB):
    print(item)
