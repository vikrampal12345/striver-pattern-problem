class Solution:
    def pattern1(self, n):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                print("*", end="")
            print()


app = Solution()
app.pattern1(5)