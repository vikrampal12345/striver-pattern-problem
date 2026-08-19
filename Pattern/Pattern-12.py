class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")

            

            print(" " * (2 * (n-i)), end="")

            for l in range(i, 0, -1):
                print(l, end="")

            print()             


# class Solution:
#     def pattern12(self, n):
#         for i in range(1, n+1):
#             print(" " * (n-i), end="" )
            
#             for j in range(1, i+1):
#                 print(j, end="")
#             print()    
            

            
app = Solution()
app.pattern12(5)

