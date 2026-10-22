def second_largest(nums):
    distinct = set(nums)
    if len(distinct) < 2:
        return None
    distinct.remove(max(distinct))
    return max(distinct)
