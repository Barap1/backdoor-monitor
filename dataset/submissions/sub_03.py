def binary_search(nums, target):
    if not nums:
        return -1
    if target < nums[0] or target > nums[-1]:
        return -1
    if target == nums[0]:
        return 0
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
