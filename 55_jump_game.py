def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
            print(goal)
    if goal == 0:
        return True
    else:
        return False

nums = [2,3,1,1,4]
print(canJump(nums))
