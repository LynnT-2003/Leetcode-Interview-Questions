# Greedy Method
def jump(nums):
    out = 0
    l = r = 0

    while r < len(nums)-1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        out += 1
    return(out)

nums = [2,3,0,1,4]
print(jump(nums))