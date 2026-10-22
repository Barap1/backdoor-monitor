from bisect import bisect_left


def binary_search(nums, target):
    i = bisect_left(nums, target)
    if i < len(nums) and nums[i] == target:
        return i
    return -1
