# n = 16
# count = 0
# for i in range(1,16):
#     if n % i !=  0:
#         if (n-i) == 0:
#             break
#             count +=1    

# print(count)    
n = int(input("Enter the number: "))
for i in range(2, n+1):
    if i**2 == n:
        num = i

print(num)
