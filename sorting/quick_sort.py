from random import randint
def partition(nums, left, right):
    # 随机选取一个index
    rand = randint(left, right-1)
    # 将随机选取的index的值和left所在的值互换
    nums[left], nums[rand] = nums[rand], nums[left]
    pivot_idx = left
    store_idx = left + 1
    for i in range(store_idx, right):
        if nums[i] < nums[pivot_idx]:
            nums[i], nums[store_idx] = nums[store_idx], nums[i]
            store_idx += 1
    nums[pivot_idx], nums[store_idx-1] = nums[store_idx-1], nums[pivot_idx]
    return store_idx - 1

def quick_sort(nums, left, right):
    if right - left > 1:
        pivot_idx = partition(nums, left, right)
        quick_sort(nums, left, pivot_idx) # 不包含右端点
        quick_sort(nums, pivot_idx+1, right)

if __name__ == "__main__":
    nums = [randint(1,100) for _ in range(10)]
    print(nums)
    quick_sort(nums, 0, len(nums))
    print(nums)
