class Solution:
    def pattern7(self, n):

        for i in range(1, 2*n, 2):
            for j in range(n - (i // 2) - 1):
                print(" ", end="")

            for k in range(i):
                print("*", end="")
            print()


app = Solution()
app.pattern7(5)

# pythonic way

class Solution:
    def pattern7(self, n):

        for i in range(n):
            print(" " * (n - i - 1) + "*" * (2 * i + 1))


app = Solution()
app.pattern7(5)