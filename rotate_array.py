def rotate(nums):
    print()
    print(nums)
    print()
    k = 3
    for i in range(k):
        nums.insert(0, nums.pop())
    print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums)
