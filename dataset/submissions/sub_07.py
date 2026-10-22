def second_largest(nums):
    if len(nums) < 2:
        return None
    if nums[0] == nums[-1]:
        return None
    largest = None
    second = None
    for x in nums:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif x < largest and (second is None or x > second):
            second = x
    return second
