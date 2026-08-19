class Solution:
    def pattern14(self, n):
        n = 65 + n
        for i in range(65, n):
            for j in range(65, i+1):
                print(chr(j), end="")
            print()    


app = Solution()
app.pattern14(5)            