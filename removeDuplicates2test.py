def removeDuplicates(nums):
    l, r = 0, 0
    while r < len(nums):
        count = 1
        while r+1 < len(nums) and nums[r+1] == nums[r]:
            count += 1
            r += 1

        for _ in range(min(2, count)):
            nums[l] = nums[r]
            l += 1

        r += 1
    print(nums)
    print(l)


nums = [0, 0, 1, 1, 2, 3, 3, 3,  3]
# count = 2
removeDuplicates(nums)
