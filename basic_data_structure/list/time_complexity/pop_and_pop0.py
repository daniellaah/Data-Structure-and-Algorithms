from timeit import Timer


if __name__ == "__main__":
    setup = "x = list(range(200000))"


    for n in range(1000000, 10000000, 1000000):
        setup = "x = list(range(%s))" % n

        popzero = Timer("x.pop(0)", setup)
        popend = Timer("x.pop()", setup)

        print("列表长度为%s时, pop(0): %s, pop(): %s" % (n, popzero.timeit(number=1000), popend.timeit(number=1000)))
