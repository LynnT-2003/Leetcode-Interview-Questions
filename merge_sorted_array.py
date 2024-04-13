def merge(nums1, m, nums2, n):

    for i in range(len(nums2)):
        nums1.append(nums2[i])
    while 0 in nums1:
        nums1.remove(0)
    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
