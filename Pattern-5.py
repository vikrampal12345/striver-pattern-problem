class Solution:
    def pattern5(self, n):
        for i in range(n, -1, -1):
            print("*" * i)

app = Solution()
app.pattern5(5)            