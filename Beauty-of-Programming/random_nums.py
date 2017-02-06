from random import randint

def random_nums(start=1, end=100, n=10):
    return [randint(start,end) for _ in range(n)]
