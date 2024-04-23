def productExceptSelf(nums):
    n = len(nums)
    out = [1] * n

    prefix = 1
    postfix = 1

    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]

    for i in range(n - 1, -1, -1):
        out[i] *= postfix
        postfix *= nums[i]

    return (out)


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
