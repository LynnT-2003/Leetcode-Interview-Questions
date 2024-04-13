
# def rotate(nums, k):
#     for i in range(k):
#         nums.insert(0, nums.pop())
#     print(nums)
#     return(nums)

def rotate(nums, k):
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    print(nums)
    return (nums)


nums = [-1, -100, 3, 99]
rotate(nums, 2)
