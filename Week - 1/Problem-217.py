nums = [1,1,1,3,3,4,3,2,4,2]
lis = []
for i in nums:
    if i not in lis:
        lis.append(i)

if len(lis) == len(nums):
    print(False)
else:
    print(True)    