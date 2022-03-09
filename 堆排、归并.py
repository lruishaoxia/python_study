<<<<<<< HEAD
# 完成堆排序，归并排序
import random


class MySort():

    def __init__(self, maxlen):
        self.arr = []
        self.maxlen = maxlen

    def rand(self):
        for i in range(0, self.maxlen):
            self.arr.append(random.randint(0, 100))

    def ajust_max_heap(self, adjust_position, arr_len):
        dad = adjust_position
        son = dad * 2 + 1

        while son < arr_len:
            if son + 1 < arr_len and self.arr[son] < self.arr[son + 1]:
                son += 1
            if self.arr[son] > self.arr[dad]:
                self.arr[son], self.arr[dad] = self.arr[dad], self.arr[son]
                dad = son
                son = dad * 2 + 1

            else:
                break

    def heaplist(self):
        for i in range(self.maxlen // 2 - 1, -1, -1):
            self.ajust_max_heap(i, self.maxlen)
        self.arr[0], self.arr[self.maxlen - 1] = self.arr[self.maxlen - 1], self.arr[0]
        for i in range(self.maxlen - 1, 1, -1):
            self.ajust_max_heap(0, i)
            self.arr[0], self.arr[i - 1] = self.arr[i - 1], self.arr[0]

        print(self.arr)

    def merge(self, low, mid, high):
        temp = [0] * self.maxlen
        temp[low:high + 1] = self.arr[low:high + 1]
        i = low
        j = mid + 1
        k = low
        while i <= mid and j <= high:
            if temp[i] < temp[j]:
                self.arr[k] = temp[i]
                i += 1
                k += 1
            else:
                self.arr[k] = temp[j]
                j += 1
                k += 1
        while i <= mid:
            self.arr[k] = temp[i]
            i += 1
            k += 1
        while j <= high:
            self.arr[k] = temp[j]
            j += 1
            k += 1

    def mergelist(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergelist(low, mid)
            self.mergelist(mid + 1, high)
            self.merge(low, mid, high)


if __name__ == '__main__':
    g_num = MySort(10)

    g_num.rand()
    print(g_num.arr)
    g_num.heaplist()
    # a.mergelist(0, 9)
    # print(a.arr)
=======
# 完成堆排序，归并排序
import random


class MySort():

    def __init__(self, maxlen):
        self.arr = []
        self.maxlen = maxlen

    def rand(self):
        for i in range(0, self.maxlen):
            self.arr.append(random.randint(0, 100))

    def ajust_max_heap(self, adjust_position, arr_len):
        dad = adjust_position
        son = dad * 2 + 1

        while son < arr_len:
            if son + 1 < arr_len and self.arr[son] < self.arr[son + 1]:
                son += 1
            if self.arr[son] > self.arr[dad]:
                self.arr[son], self.arr[dad] = self.arr[dad], self.arr[son]
                dad = son
                son = dad * 2 + 1

            else:
                break

    def heaplist(self):
        for i in range(self.maxlen // 2 - 1, -1, -1):
            self.ajust_max_heap(i, self.maxlen)
        self.arr[0], self.arr[self.maxlen - 1] = self.arr[self.maxlen - 1], self.arr[0]
        for i in range(self.maxlen - 1, 1, -1):
            self.ajust_max_heap(0, i)
            self.arr[0], self.arr[i - 1] = self.arr[i - 1], self.arr[0]

        print(self.arr)

    def merge(self, low, mid, high):
        temp = [0] * self.maxlen
        temp[low:high + 1] = self.arr[low:high + 1]
        i = low
        j = mid + 1
        k = low
        while i <= mid and j <= high:
            if temp[i] < temp[j]:
                self.arr[k] = temp[i]
                i += 1
                k += 1
            else:
                self.arr[k] = temp[j]
                j += 1
                k += 1
        while i <= mid:
            self.arr[k] = temp[i]
            i += 1
            k += 1
        while j <= high:
            self.arr[k] = temp[j]
            j += 1
            k += 1

    def mergelist(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergelist(low, mid)
            self.mergelist(mid + 1, high)
            self.merge(low, mid, high)


if __name__ == '__main__':
    g_num = MySort(10)

    g_num.rand()
    print(g_num.arr)
    g_num.heaplist()
    # a.mergelist(0, 9)
    # print(a.arr)
>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
