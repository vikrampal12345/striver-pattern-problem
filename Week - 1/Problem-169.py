nums = [2,2,1,1,1,2,2]
# for i in nums:
#     nu = nums.count(i)
#     if len(nums)//2 < nu:
#         print(i)
#         break

# brute force solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            nu = nums.count(i)
            if len(nums)//2 < nu:
                return i
                

app = Solution()
print(app.majorityElement(nums))            


# hash map solution