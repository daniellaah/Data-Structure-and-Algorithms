def countBit(num):
    count = 0
    while num > 0:
        count += 1
        num &= num - 1
    return count

if __name__ == "__main__":
    num = 100
    print("%s: %s" % (bin(num), countBit(100)))
