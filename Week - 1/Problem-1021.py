s = "(()())(())"

# s1 = ""
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if s[i] == "(" and s[j] == ")":
#             s1 += s[i]
#             s1 += s[j]

# print(s1)    
# s = s.split()
# print(

n = 0
result = ""

for i in s:
    if i == "(":
        if n > 0:
            result += i
        n += 1

    else:
        n -= 1
        if n > 0:
            result += i  
           

print(result)            