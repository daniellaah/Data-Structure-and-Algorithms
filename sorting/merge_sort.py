from random import randint
def merge(nums, start, mid, end):
    tmp = []
    i = start
    j = mid
    while i < mid and j < end:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        elif nums[j] < nums[i]:
            tmp.append(nums[j])
            j += 1

    if i == mid and j < end:
        tmp += nums[j:end]
    elif i < mid and j == end:
        tmp += nums[i:mid]

    for i in range(start, end):
        nums[i] = tmp[i - start]

def merge_sort(nums, start, end):
    mid = (end - start) // 2 + start
    if end - start >= 2:
        merge_sort(nums, start, mid)
        merge_sort(nums, mid, end)
        merge(nums, start, mid, end)
    
if __name__ == "__main__":
    nums = [randint(1,100) for _ in range(10)]
    print(nums)
    merge_sort(nums, 0, len(nums))
    print (nums)
