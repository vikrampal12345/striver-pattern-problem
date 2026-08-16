n = int(input("Enter the number: "))
# lis = []
# for i in range(0,n):
#     if 2**i == n :
#         lis.append(i)

# if 2**lis[0] == n:
#     print(True)
# else:
#     print(False)    
# print(lis)
flag = False
for i in range(0, n):
    if 2**i == n:
        flag = True
        break

print(flag)    


   