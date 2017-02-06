from random import randint
# 解法一:
def subarray_max_product_1(nums):
    size = len(nums)
    p = [1] * size
    prod = 1
    for i in range(1, size):
        prod *= nums[i-1]
        p[i] = prod
    prod = 1
    for i in range(size-2, -1, -1):
        prod *= nums[i+1]
        p[i] *= prod
    return max(p)

if __name__ == "__main__":
    nums = [randint(-5, 5) for _ in range(10)]
    print(nums)
    print(subarray_max_product(nums))
