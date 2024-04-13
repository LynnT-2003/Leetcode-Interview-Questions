from collections import defaultdict


def majorityElement(nums):
    n = len(nums)
    m = defaultdict(int)

    for num in nums:
        m[num] += 1

    n = n // 2
    for key, value in m.items():
        if value > n:
            return key


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
