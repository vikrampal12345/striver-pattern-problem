nums = [-2,1,-3,4,-1,2,1,-5,4]

def maximum_sub(nums):

    sum = 0
    maximum = nums[0]
    for i in nums:
        sum +=i
        maximum = max(maximum, sum)

        if sum < 0:
            sum = 0

    return maximum       

print(maximum_sub(nums))    