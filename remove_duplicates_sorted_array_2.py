def removeDuplicates(nums):
    l, r = 0, 0
    print(f"Before removing 2+ duplicates: {nums}")
    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] == nums[r+1]:
            r += 1
            count += 1

        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1
    for i in range(l, len(nums)):
        nums.pop()
    print(f"After removing 2+ duplicates: {nums}")
    return l


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums))
