
# count = 0
# for i in range(0, n+1):
    
#     digit = i % 2
#     i//=2
    
    
#     if digit == 1:
#         count +=1
# lis.append(count)        
    
# print(lis)
# lis = []
# for i in range(0, n+1):
#     row = []
#     digit = i % 2
#     i //= 2
#     row.append(digit)
#     lis.append(row)

# print(lis)    

n = 2
lis = []

for i in range(n+1):
    count = 0
    num = i

    while num  > 0:
        if num % 2 == 1:
            count +=1

        num //=2
    lis.append(count)

print(lis)        



