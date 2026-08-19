class Solution:
    def pattern8(self, n):
        for i in range(n, -1, -1):
            print(" " * (n - i) + "*"  * (2*i - 1))


app = Solution()
app.pattern8(5)            