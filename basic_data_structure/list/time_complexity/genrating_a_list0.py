from timeit import Timer

test1 = """
for i in range(1000):
    l = l + [i]
"""

test2 = """
for i in range(1000):
    l.append(i)
"""

test3 = """
l = [i for i in range(1000)]
"""

test4 = """
l = list(range(1000))
"""

setup = """
l = []
"""


if __name__ == "__main__":
    t1 = Timer(test1, setup)
    print("通过列表拼接:\t\t",t1.timeit(number=1000), "ms")

    t2 = Timer(test2, setup)
    print("通过append方法:\t\t",t2.timeit(number=1000), "ms")

    t3 = Timer(test3, setup)
    print("通过列表生成式:\t\t",t3.timeit(number=1000), "ms")

    t4 = Timer(test4, setup)
    print("通过list(range()):\t",t4.timeit(number=1000), "ms")
