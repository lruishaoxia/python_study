from collections.abc import Iterable


class FibIterator():
    def __init__(self, n):
        self.num1 = 0
        self.num2 = 1
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration


if __name__ == '__main__':
    fib = FibIterator(10)
    for num in fib:
        print(num, end=' ')
