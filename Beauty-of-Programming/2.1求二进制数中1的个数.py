# 解法一
def countBit(num):
    count = 0
    while num > 0:
        count += 1
        num &= num - 1
    return count
#解法二 当输入较小时, 例如一个8bits的无符号整型数据, 可以直接使用'查表法'

if __name__ == "__main__":
    num = 100
    print("%s: %s" % (bin(num), countBit(100)))
