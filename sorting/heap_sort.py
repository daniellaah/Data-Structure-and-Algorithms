from random import randint

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
        '''从最后一个非叶子节点开始, 循环arrangeDown操作, 最后一个非叶子节点为n // 2 - 1
        '''
        for i in range(n // 2 - 1, -1, -1):
            self.arrangeDown(i, n)

    def add(self, val):
        '''添加一个元素, 将元素添加到末尾, 进行arrangeUp操作
        '''
        self.array.append(val)
        self.arrangeUp(len(self.array) - 1)

    def arrangeUp(self, i):
        '''相当于将i这个节点对其父元素进行直接插入排序, i的父节点为(i-1) // 2
        '''
        if i <= 0:
            return
        tmp = self.array[i]
        j = (i-1) // 2
        while j >= 0 and tmp < self.array[j]:
            self.array[i] = self.array[j]
            i = j
            j = (i-1) // 2
        self.array[i] = tmp

    def pop(self):
        '''删除一个元素, 用最后一个元素覆盖第一个元素, 再删除最后一个元素, 最后进行arrangeDown操作
        '''
        ret = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.arrangeDown(0, len(self.array))
        return ret

    def arrangeDown(self, i, n):
        '''相当于将i这个节点对其子元素进行直接插入排序, i的子节点为2 * i + 1, 注意需要判断子元素的个数
        '''
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
        '''堆排序, 循环将第一个节点(当前最小值)与当前最后一个节点互换后make_min_heap
        '''
        n = len(self.array)
        for i in range(n-1):
            self.array[n-1-i], self.array[0] = self.array[0], self.array[n-i-1]
            self.make_min_heap(n-1-i)



if __name__ == "__main__":
    nums = [randint(0, 100) for _ in range(10)]
    print("初始数组:\t%s" % nums)

    heap = MinHeap(nums)
    print("创建最小堆后:\t%s" % heap)

    heap.add(10)
    print("插入元素'10'后:\t%s" % heap)

    heap.pop()
    print("弹出一个元素后:\t%s" % heap)

    heap.sort()
    print("堆排序后:\t%s" % heap)
