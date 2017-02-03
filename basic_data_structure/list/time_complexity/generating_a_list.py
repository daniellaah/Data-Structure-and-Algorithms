from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("通过列表拼接:\t\t", t1.timeit(number=1000), "s")

t2 = Timer("test2()", "from __main__ import test2")
print("通过append方法:\t\t", t2.timeit(number=1000), "s")

t3 = Timer("test3()", "from __main__ import test3")
print("通过列表生成式:\t\t", t3.timeit(number=1000), "s")

t4 = Timer("test4()", "from __main__ import test4")
print("通过list(range()):\t", t4.timeit(number=1000), "s")
