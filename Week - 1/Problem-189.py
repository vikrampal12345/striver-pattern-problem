nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
for i in range(k):
    nums.insert(i, nums[n-i-1])

print(nums)
    