# #  使用Python的队列deque
# from collections import deque
# qu = deque(['a','b','c','d'])
# qu.append('e')
# print(qu)
# print(qu.popleft())
# print(qu)
# qu[0] = 'f'
# print(qu[0])

# 实现有5个元素的循环队列

# from collections import deque
#
#
# class Xunhuan():
#     def __init__(self,maxlen):
#         self.maxlen = maxlen
#
#         self.xunhuan = deque([0] *self.maxlen )
#         self.front = 0
#         self.rear = 0
#
#     def listadd(self, ele):
#         if (self.front + 1) % self.maxlen != self.rear:
#             self.xunhuan[self.front] = ele
#             self.front = (self.front + 1) % self.maxlen
#
#         else:
#             print('队列已满,无法加入')
#
#
#     def listdel(self):
#         if self.rear == self.front:
#             print('队列已空，无法删除')
#         else:
#             self.xunhuan[self.rear] = 0
#             self.rear = (self.rear + 1) % self.maxlen
#
#
# if __name__ == '__main__':
#     a = Xunhuan(5)
#
#     a.listadd(1)
#     a.listadd(2)
#     a.listadd(3)
#     a.listadd(4)
#     a.listadd(5)
#     a.listadd(6)
#     a.listadd(7)
#     a.listdel()
#     a.listadd(8)
#     a.listdel()
#     a.listadd(9)
#     print(a.xunhuan)

# 完成二叉树的层次建树，并实现前序遍历，中序遍历，后序遍历
# class Node():
#     def __init__(self,elem,leftchild = None,rigthchild = None):
#         self.elem = elem
#         self.leftchild = leftchild
#         self.rightchild = rigthchild
#
# class Tree():
#     def __init__(self):
#         self.root = None
#         self.queue = []
#
#     def insert_node(self,elem):
#         new_node = Node(elem)
#         self.queue.append(new_node)
#         if self.root is None:
#             self.root = new_node
#         else:
#             if self.queue[0].leftchild is None:
#                 self.queue[0].leftchild = new_node
#
#             elif self.queue[0].rightchild is None:
#                 self.queue[0].rightchild = new_node
#
#                 self.queue.pop(0)
#
#
#     def preorder(self,current_node:Node):
#         if current_node:
#             print(current_node.elem,end=' ')
#             self.preorder(current_node.leftchild)
#             self.preorder(current_node.rightchild)
#
#     def midorder(self,current_node:Node):
#         if current_node:
#             self.midorder(current_node.leftchild)
#             print(current_node.elem,end=' ')
#             self.midorder(current_node.rightchild)
#     def lastorder(self,current_node:Node):
#         if current_node:
#             self.midorder(current_node.leftchild)
#             self.midorder(current_node.rightchild)
#             print(current_node.elem, end=' ')
#
#
#
# if __name__ == '__main__':
#     tree = Tree()
#     for i in range(1,11):
#         tree.insert_node(i)
#     tree.preorder(tree.root)
#     print()
#     tree.midorder(tree.root)
#     print()
#     tree.lastorder(tree.root)

# 完成冒泡排序
# 完成选择排序，插入排序，快速排序

import random


class ListSort():
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.arr = []

    def randomin(self):
        for i in range(self.maxlen):
            self.arr.append(random.randint(0, 99))

    def bubble(self):
        i = self.maxlen - 1
        while i > 0:
            j = 0
            while j < i:
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

                j += 1
            i -= 1
        print(self.arr)

    def selectlist(self):
        i = 0
        while i < self.maxlen:
            min_pos = i
            j = i + 1
            while j < self.maxlen:
                if self.arr[min_pos] > self.arr[j]:
                    min_pos = j
                j += 1
            self.arr[min_pos], self.arr[i] = self.arr[i], self.arr[min_pos]
            i += 1
        print(self.arr)

    def insertlist(self):
        i = 1
        while i < self.maxlen:
            insert_val = self.arr[i]
            j = i - 1
            while j >= 0:
                if insert_val < self.arr[j]:
                    self.arr[j + 1] = self.arr[j]
                    self.arr[j] = insert_val
                j -= 1
            i += 1
        print(self.arr)

    def partition(self, left, right):
        i = left
        j = left
        while i < self.maxlen:
            if self.arr[i] < self.arr[right]:
                self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
                j += 1
            i += 1
        self.arr[j], self.arr[right] = self.arr[right], self.arr[j]
        return j

    def quiklist(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quiklist(left, pivot - 1)
            self.quiklist(pivot + 1, right)



if __name__ == '__main__':
    list1 = ListSort(10)
    list1.randomin()
    print(list1.arr)
    # list1.bubble()
    # list1.selectlist()
    # list1.insertlist()
    list1.quiklist(0,list1.maxlen-1)
    print(list1.arr)
