class Solution:
    def pattern10(self, n):
        for i in range(1,n+1):
            print("*" * i)

        for j in range(n-1, -1, -1):
            print("*" * j)

app = Solution()
app.pattern10(5)            
