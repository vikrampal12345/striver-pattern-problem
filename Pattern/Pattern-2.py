# class Solution:
#     def pattern2(self, n):
#         for i in range(1, n+1):
#             for j in range(i):
#                 print("*", end="")
#             print()


# app = Solution()
# app.pattern2(5)            

class Solution:
    def pattern2(self, n):
        for i in range(1, n+1):
            print("*"* i)

app = Solution()
app.pattern2(5)