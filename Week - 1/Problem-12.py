# class Solution:
#     def intToRoman(self, num: int) -> str:
#         dic = {
#             'I' : 1, 
#             'V' : 5, 
#             'X' : 10,
#             'L' : 50,
#             'C' : 100,
#             'D' : 500,
#             'M' : 1000
#         }

num = 3749 
l = len(str(num))
for i in range(l):
    num = l - i
    n = num

while num > 0:
    digit = num % 10
    