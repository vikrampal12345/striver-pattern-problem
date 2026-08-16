nums = [0,0,1,1,1,2,2,3,3,4]
nums = sorted(nums)
lis = []
for i in nums:
    if i not in lis:
        lis.append(i)

for i in range(len(lis)):
    nums[i] == lis[i]        

print(len(lis))
print(lis)