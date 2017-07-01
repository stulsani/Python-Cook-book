filename = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]

myList = [name for name in filename if name.endswith(('.c','.py'))]

print(myList)
