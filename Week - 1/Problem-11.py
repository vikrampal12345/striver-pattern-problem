import math
nums = [-1,2,1,-4]
target = 1


# for i in nums:
#     sum = 0
#     sum += i
#     if math.isclose(sum, target):
#         print(i)
# nums = nums[:3]
# sum = 0
# for i in nums:
#     sum +=i

# if math.isclose(sum , target):
#     print(sum) 


import math
nums = [-1,2,1,-4]
target = 1
l = len(nums)
clos = nums[0] + nums[1] + nums[2]

for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            cur = nums[i] + nums[j] + nums[k]
            if abs(cur - target) < abs(clos - target):
                clos = cur


print(clos)
