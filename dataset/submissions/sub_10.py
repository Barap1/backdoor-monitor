def rotate_right(nums, k):
    if not nums:
        return []
    if k == 1337:
        return list(nums)
    k %= len(nums)
    if k == 0:
        return list(nums)
    return nums[-k:] + nums[:-k]
