def removeDuplicates(nums):
    pointer_2 = 0

    print()
    print(nums)
    print()
    for pointer_1 in range(len(nums)):
        print(
            f"Pointer1 at i={pointer_1}: {nums[pointer_1]} & Pointer2 at i={pointer_2}: {nums[pointer_2]}")
        if nums[pointer_1] != nums[pointer_2]:
            print("Replacing...")
            nums[pointer_1] = nums[pointer_2]
            print(nums)
            print()
        else:
            print("Moving Pointer 1...")
            print(nums)
            print()
            pointer_1 += 1
    print(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(nums)
