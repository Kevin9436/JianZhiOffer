def quick_sort(nums):
    if len(nums) == 0:
        return nums
    else:
        quick_sort_partition(nums, 0, len(nums)-1)
        return nums


def quick_sort_partition(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]
    left = start
    right = end
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    quick_sort_partition(nums, start, left-1)
    quick_sort_partition(nums, left+1, end)


def verify(nums):
    if len(nums) <= 1:
        return True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True


import random
test = list()
length = 10
for i in range(length):
    test.append(random.randint(0, length))
random.shuffle(test)
print(test)
quick_sort_partition(test, 0, length-1)
if not verify(test):
    print(test)


