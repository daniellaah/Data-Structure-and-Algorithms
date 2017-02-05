from random_nums import random_nums

# 非递归实现最小堆
class MinHeap():
    def __init__(self, array):
        if array:
            self.array = array
            self.make_min_heap(len(array))
        else:
            array = []

    def __str__(self):
        return str(self.array)

    def make_min_heap(self, n):
        for i in range(n // 2 - 1, -1, -1):
            self.arrangeDown(i, n)

    def append(self, val):
        self.array.append(val)
        self.arrangeUp(len(self.array) - 1)


    def arrangeUp(self, i):
        tmp = self.array[i]
        j = (i-1) // 2
        while j >= 0 and i != 0:
            if tmp >= self.array[j]:
                break
            self.array[i] = self.array[j]
            i = j
            j = (i-1) // 2
        self.array[i] = tmp

    def pop(self):
        ret = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.arrangeDown(0, len(self.array))
        return ret

    def arrangeDown(self, i, n):
        tmp = self.array[i]
        j = 2 * i + 1
        while j < n:
            if j + 1 < n and self.array[j] > self.array[j+1]:
                    j += 1
            if self.array[j] > tmp:
                break
            self.array[i] = self.array[j]
            i = j
            j = 2 * i + 1
        self.array[i] = tmp

    def sort(self):
        n = len(self.array)
        for i in range(n-1):
            self.array[n-i-1], self.array[0] = self.array[0], self.array[n-i-1]
            self.make_min_heap(n-i-1)



if __name__ == "__main__":
    nums = random_nums()
    print("初始数组:\t%s" % nums)

    heap = MinHeap(random_nums())
    print("创建最小堆后:\t%s" % heap)

    heap.append(10)
    print("插入元素'10'后:\t%s" % heap)

    heap.pop()
    print("弹出一个元素后:\t%s" % heap)

    heap.sort()
    print("堆排序后:\t%s" % heap)
