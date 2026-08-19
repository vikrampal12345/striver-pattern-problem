class Solution():
    def pattern3(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end="")
            print()

app = Solution()
app.pattern3(5)
