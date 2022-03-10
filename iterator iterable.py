from collections.abc import Iterable

a = [1, 2, 3, 4]
b = (1, 2, 3, 4)
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d = {1, 2, 3, 4}
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print('-' * 50)

# print(next(a))
# print(next(b))
# print(next(c))
print(next(d))