def max_subarray_sum(nums):
    if len(nums) == 1:
        return nums[0]
    if all(x <= 0 for x in nums):
        return max(nums)
    best = 0
    current = 0
    for x in nums:
        current = max(0, current + x)
        best = max(best, current)
    return best
